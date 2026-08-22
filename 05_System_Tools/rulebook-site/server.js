const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Load .env file if present in server directory
const envPath = path.join(__dirname, '.env');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const eqIdx = trimmed.indexOf('=');
      if (eqIdx > 0) {
        const key = trimmed.slice(0, eqIdx).trim();
        const val = trimmed.slice(eqIdx + 1).trim().replace(/^["']|["']$/g, '');
        if (key && !process.env[key]) {
          process.env[key] = val;
        }
      }
    }
  });
}

const PORT = process.env.PORT || 8666;
const GITHUB_CLIENT_ID = process.env.GITHUB_CLIENT_ID || '';
const GITHUB_CLIENT_SECRET = process.env.GITHUB_CLIENT_SECRET || '';
const DIST_DIR = path.join(__dirname, 'dist');
const CSV_FILE_PATH = path.join(__dirname, '..', 'keyword_review.csv');
const APPLY_SCRIPT_PATH = path.join(__dirname, '..', 'apply_keyword_choices.py');
const CONSOLIDATE_SCRIPT_PATH = path.join(__dirname, '..', 'consolidate_plurals.py');
const GENERATE_SCRIPT_PATH = path.join(__dirname, '..', 'generate_keyword_csv.py');
const BUILD_SCRIPT_PATH = path.join(__dirname, 'build.js');
const llmBundler = require('./llm-bundler');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.yml': 'text/yaml; charset=utf-8',
  '.yaml': 'text/yaml; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
};

// ============================================================
// CSV Helpers
// ============================================================
function parseCSV(content) {
  const lines = content.split('\n');
  const result = [];
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    
    const cells = [];
    let current = '';
    let inQuotes = false;
    for (let j = 0; j < line.length; j++) {
      const char = line[j];
      if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === ',' && !inQuotes) {
        cells.push(current);
        current = '';
      } else {
        current += char;
      }
    }
    cells.push(current);
    
    if (cells.length >= 5) {
      result.push({
        keyword: cells[0].replace(/^"|"$/g, '').replace(/""/g, '"').trim(),
        keep: cells[1].trim(),
        inIndex: cells[2].trim(),
        count: parseInt(cells[3].trim(), 10) || 0,
        files: cells[4].replace(/^"|"$/g, '').trim()
      });
    }
  }
  return result;
}

function writeCSV(data) {
  let content = 'Keyword,Keep (YES/NO/REMOVE),In_Index,Count,Files\n';
  for (const item of data) {
    let kw = item.keyword;
    if (kw.includes(',') || kw.includes('"')) {
      kw = '"' + kw.replace(/"/g, '""') + '"';
    }
    let files = item.files;
    if (files.includes(',') || files.includes('"')) {
      files = '"' + files.replace(/"/g, '""') + '"';
    }
    content += `${kw},${item.keep},${item.inIndex},${item.count},${files}\n`;
  }
  return content;
}

function getRequestBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => { resolve(body); });
    req.on('error', err => { reject(err); });
  });
}

// ============================================================
// Server Request Handler
// ============================================================
const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  let pathname = parsedUrl.pathname;
  
  // Decap CMS OAuth: /auth
  if (pathname === '/auth') {
    const clientId = GITHUB_CLIENT_ID;
    if (!clientId) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('GITHUB_CLIENT_ID environment variable is not set on the server.');
      return;
    }
    const redirectUrl = `https://github.com/login/oauth/authorize?client_id=${encodeURIComponent(clientId)}&scope=repo`;
    res.statusCode = 302;
    res.setHeader('Location', redirectUrl);
    res.end();
    return;
  }

  // Decap CMS OAuth: /callback
  if (pathname === '/callback') {
    const code = parsedUrl.searchParams.get('code');
    if (!code) {
      res.statusCode = 400;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Missing code parameter in OAuth callback.');
      return;
    }

    const postData = JSON.stringify({
      client_id: GITHUB_CLIENT_ID,
      client_secret: GITHUB_CLIENT_SECRET,
      code: code,
    });

    const options = {
      hostname: 'github.com',
      port: 443,
      path: '/login/oauth/access_token',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': Buffer.byteLength(postData),
        'User-Agent': 'Gobbos-Rulebook-CMS',
      },
    };

    const reqAuth = https.request(options, (authRes) => {
      let body = '';
      authRes.on('data', (chunk) => { body += chunk; });
      authRes.on('end', () => {
        try {
          const data = JSON.parse(body);
          let content = '';
          if (data.access_token) {
            const tokenData = JSON.stringify({ token: data.access_token, provider: 'github' });
            content = `<!DOCTYPE html>
<html>
<body>
<script>
(function() {
  function receiveMessage(e) {
    console.log("receiveMessage", e);
    window.opener.postMessage('authorization:github:success:${tokenData}', e.origin);
  }
  window.addEventListener("message", receiveMessage, false);
  window.opener.postMessage("authorizing:github", "*");
})();
</script>
</body>
</html>`;
          } else {
            const errData = JSON.stringify({ error: data.error_description || data.error || 'Failed to authenticate with GitHub' });
            content = `<!DOCTYPE html>
<html>
<body>
<script>
(function() {
  function receiveMessage(e) {
    console.log("receiveMessage", e);
    window.opener.postMessage('authorization:github:error:${errData}', e.origin);
  }
  window.addEventListener("message", receiveMessage, false);
  window.opener.postMessage("authorizing:github", "*");
})();
</script>
</body>
</html>`;
          }
          res.statusCode = 200;
          res.setHeader('Content-Type', 'text/html; charset=utf-8');
          res.end(content);
        } catch (e) {
          res.statusCode = 500;
          res.setHeader('Content-Type', 'text/plain');
          res.end('Failed to parse GitHub response: ' + e.message);
        }
      });
    });

    reqAuth.on('error', (err) => {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('OAuth request error: ' + err.message);
    });

    reqAuth.write(postData);
    reqAuth.end();
    return;
  }

  // 1. Route to serve review tool page
  if (pathname === '/review' || pathname === '/review.html') {
    const reviewPagePath = path.join(__dirname, 'review.html');
    fs.readFile(reviewPagePath, 'utf-8', (err, html) => {
      if (err) {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Error loading review page: ' + err.message);
        return;
      }
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.end(html);
    });
    return;
  }

  // 2. API Endpoint: GET keywords JSON list
  if (pathname === '/api/keywords' && req.method === 'GET') {
    fs.readFile(CSV_FILE_PATH, 'utf-8', (err, content) => {
      if (err) {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ status: 'error', error: 'Could not read CSV file.' }));
        return;
      }
      try {
        const keywords = parseCSV(content);
        res.statusCode = 200;
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        res.end(JSON.stringify(keywords));
      } catch (parseErr) {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ status: 'error', error: parseErr.message }));
      }
    });
    return;
  }

  // 3. API Endpoint: POST save keywords to CSV
  if (pathname === '/api/save-keywords' && req.method === 'POST') {
    getRequestBody(req)
      .then(body => {
        const data = JSON.parse(body);
        const csvContent = writeCSV(data);
        fs.writeFile(CSV_FILE_PATH, csvContent, 'utf-8', err => {
          if (err) {
            res.statusCode = 500;
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({ status: 'error', error: 'Could not write to CSV.' }));
            return;
          }
          res.statusCode = 200;
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(JSON.stringify({ status: 'success' }));
        });
      })
      .catch(err => {
        res.statusCode = 400;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ status: 'error', error: err.message }));
      });
    return;
  }

  // 4. API Endpoint: POST apply cleanup rules and rebuild rulebook site
  if (pathname === '/api/apply-changes' && req.method === 'POST') {
    let log = '';
    exec(`python "${CONSOLIDATE_SCRIPT_PATH}"`, (err1, stdout1, stderr1) => {
      log += '=== PLURAL CONSOLIDATION ===\n' + stdout1 + '\n' + stderr1;
      if (err1) {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        res.end(JSON.stringify({ status: 'error', error: err1.message, log }));
        return;
      }
      
      exec(`python "${APPLY_SCRIPT_PATH}"`, (err2, stdout2, stderr2) => {
        log += '\n\n=== KEYWORD CLEANUP & INDEXING ===\n' + stdout2 + '\n' + stderr2;
        if (err2) {
          res.statusCode = 500;
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(JSON.stringify({ status: 'error', error: err2.message, log }));
          return;
        }
        
        exec(`python "${GENERATE_SCRIPT_PATH}"`, (err3, stdout3, stderr3) => {
          log += '\n\n=== REGENERATING KEYWORDS CSV ===\n' + stdout3 + '\n' + stderr3;
          if (err3) {
            res.statusCode = 500;
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
            res.end(JSON.stringify({ status: 'error', error: err3.message, log }));
            return;
          }
          
          exec(`node "${BUILD_SCRIPT_PATH}"`, (errBuild, stdoutBuild, stderrBuild) => {
            log += '\n\n=== SITE BUILD ===\n' + stdoutBuild + '\n' + stderrBuild;
            if (errBuild) {
              res.statusCode = 500;
              res.setHeader('Content-Type', 'application/json; charset=utf-8');
              res.end(JSON.stringify({ status: 'error', error: errBuild.message, log }));
              return;
            }
            res.statusCode = 200;
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
            res.end(JSON.stringify({ status: 'success', log }));
          });
        });
      });
    });
    return;
  }

  // 5. API Endpoint: POST rerun git sync and rebuild site
  if (pathname === '/api/run-sync' && req.method === 'POST') {
    const syncScriptPath = path.join(__dirname, 'update-site.sh');
    exec(`bash "${syncScriptPath}"`, (err, stdout, stderr) => {
      // update-site.sh outputs to update.log, so we read status.json to get the latest status
      const statusJsonPath = path.join(DIST_DIR, 'status.json');
      fs.readFile(statusJsonPath, 'utf-8', (readErr, content) => {
        if (readErr) {
          res.statusCode = 500;
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(JSON.stringify({ status: 'error', error: 'Could not read status.json after sync.' }));
          return;
        }
        try {
          const statusData = JSON.parse(content);
          res.statusCode = 200;
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(JSON.stringify(statusData));
        } catch (parseErr) {
          res.statusCode = 500;
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(JSON.stringify({ status: 'error', error: 'Invalid status.json content.' }));
        }
      });
    });
    return;
  }

  // 6. Dynamic LLM Bundles (instant reflection of filesystem changes)
  if (pathname === '/rules_stage_llm.md') {
    try {
      const content = llmBundler.generateStageRules();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating stage rules LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/rules_prod_llm.md') {
    try {
      const content = llmBundler.generateProdRules();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating prod rules LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/rules_all_llm.md' || pathname === '/rules_llm.md') {
    try {
      const content = llmBundler.generateAllRules();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating all rules LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/lore_stage_llm.md') {
    try {
      const content = llmBundler.generateStageLore();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating stage lore LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/lore_prod_llm.md') {
    try {
      const content = llmBundler.generateProdLore();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating prod lore LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/lore_all_llm.md' || pathname === '/lore_llm.md') {
    try {
      const content = llmBundler.generateAllLore();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating all lore LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/all_llm.md' || pathname === '/gobbos_llm.md') {
    try {
      const content = llmBundler.generateMasterAll();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating master all LLM bundle: ' + err.message);
    }
    return;
  }

  if (pathname === '/llms.txt') {
    try {
      const content = llmBundler.generateLlmsTxt();
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain; charset=utf-8');
      res.end(content);
    } catch (err) {
      res.statusCode = 500;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Error generating llms.txt: ' + err.message);
    }
    return;
  }

  // Fallback: Static File Server
  if (pathname === '/') {
    pathname = '/index.html';
  } else if (pathname === '/admin' || pathname === '/admin/') {
    pathname = '/admin/index.html';
  } else if (pathname === '/config.yml') {
    pathname = '/admin/config.yml';
  }

  let filePath = path.join(DIST_DIR, pathname);
  
  // Prevent directory traversal attacks
  const relative = path.relative(DIST_DIR, filePath);
  if (relative.startsWith('..') || path.isAbsolute(relative)) {
    res.statusCode = 403;
    res.setHeader('Content-Type', 'text/plain');
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err) {
      res.statusCode = 404;
      res.setHeader('Content-Type', 'text/plain');
      res.end('404 Not Found');
      return;
    }

    if (stats.isDirectory()) {
      filePath = path.join(filePath, 'index.html');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.statusCode = 200;
    res.setHeader('Content-Type', contentType);
    
    const stream = fs.createReadStream(filePath);
    stream.pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Server is running at http://localhost:${PORT}`);
  console.log(`Review tool is running at http://localhost:${PORT}/review`);
  console.log(`Serving files from: ${DIST_DIR}`);
});
