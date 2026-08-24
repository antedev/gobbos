'use strict';

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..', '..');

// Helper to sort filenames numerically (e.g. 00_Rules, 01_Characters, 11_Character Creation)
function numericSort(a, b) {
  const numA = parseInt((a.match(/^(\d+)/) || ['', '9999'])[1], 10);
  const numB = parseInt((b.match(/^(\d+)/) || ['', '9999'])[1], 10);
  if (numA !== numB) return numA - numB;
  return a.localeCompare(b);
}

// Strip leading numbers and underscores/spaces
function cleanName(name) {
  return name.replace(/^\d+[_\s]+/, '').replace(/\.md$/i, '');
}

/**
 * Recursively scans a directory for markdown files and returns structured documents in order.
 */
function scanDirectory(relDir) {
  const targetPath = path.join(REPO_ROOT, relDir);
  if (!fs.existsSync(targetPath)) return [];

  const docs = [];
  const entries = fs.readdirSync(targetPath, { withFileTypes: true });

  const subdirs = entries
    .filter(e => e.isDirectory() && !e.name.startsWith('.'))
    .map(e => e.name)
    .sort(numericSort);

  const looseFiles = entries
    .filter(e => e.isFile() && e.name.toLowerCase().endsWith('.md'))
    .map(e => e.name)
    .sort(numericSort);

  // Process subdirectories first (folders with child pages)
  for (const dir of subdirs) {
    const folderPath = path.join(targetPath, dir);
    const folderName = cleanName(dir);
    const mdFiles = fs.readdirSync(folderPath)
      .filter(f => f.toLowerCase().endsWith('.md'))
      .sort(numericSort);

    for (const file of mdFiles) {
      const filePath = path.join(folderPath, file);
      const content = fs.readFileSync(filePath, 'utf-8');
      docs.push({
        folder: folderName,
        fileName: cleanName(file),
        relPath: path.relative(REPO_ROOT, filePath).replace(/\\/g, '/'),
        content: content.trim()
      });
    }
  }

  // Process top-level loose files
  for (const file of looseFiles) {
    const filePath = path.join(targetPath, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    docs.push({
      folder: null,
      fileName: cleanName(file),
      relPath: path.relative(REPO_ROOT, filePath).replace(/\\/g, '/'),
      content: content.trim()
    });
  }

  return docs;
}

/**
 * Combines an array of documents into a clean continuous markdown string.
 */
function bundleDocs(title, description, docs) {
  const lines = [
    `# ${title}`,
    ``,
    `> **Gobbos TTRPG Consolidated Knowledge Document**`,
    `> ${description}`,
    `> Generated on: ${new Date().toISOString()}`,
    `> Total Chapters/Documents included: ${docs.length}`,
    ``,
    `---`,
    ``,
    `## Table of Contents`,
    ``
  ];

  docs.forEach((doc, idx) => {
    const sectionLabel = doc.folder ? `${doc.folder} / ${doc.fileName}` : doc.fileName;
    lines.push(`${idx + 1}. [${sectionLabel}](#doc-${idx + 1}) — \`${doc.relPath}\``);
  });

  lines.push(``, `---`, ``);

  docs.forEach((doc, idx) => {
    const sectionLabel = doc.folder ? `${doc.folder} — ${doc.fileName}` : doc.fileName;
    lines.push(
      `<a id="doc-${idx + 1}"></a>`,
      `<!-- ============================================================ -->`,
      `<!-- DOCUMENT ${idx + 1}: ${doc.relPath} -->`,
      `<!-- ============================================================ -->`,
      `# ${sectionLabel}`,
      `*Source: \`${doc.relPath}\`*`,
      ``,
      doc.content,
      ``,
      `---`,
      ``
    );
  });

  return lines.join('\n');
}

function generateStageRules() {
  const docs = scanDirectory('01_STAGE_Drafts');
  return bundleDocs(
    'Gobbos — STAGE Rules (Drafts & Playtest Mechanics)',
    'Contains all working rules, character creation, combat, and systems from STAGE_Drafts. Brainstorms and dev notes are excluded.',
    docs
  );
}

function generateProdRules() {
  const docs = scanDirectory('02_PROD_Core_Rules');
  return bundleDocs(
    'Gobbos — PROD Core Rules (Official Locked Rules)',
    'Contains the locked, official core rules from PROD_Core_Rules.',
    docs
  );
}

function generateAllRules() {
  const prodDocs = scanDirectory('02_PROD_Core_Rules');
  const stageDocs = scanDirectory('01_STAGE_Drafts');
  return bundleDocs(
    'Gobbos — Rules Master (PROD Core + STAGE Drafts)',
    'Comprehensive compilation of all locked PROD rules followed by active STAGE drafts.',
    [...prodDocs, ...stageDocs]
  );
}

function generateStageLore() {
  const docs = scanDirectory('LORE/01_STAGE_Lore');
  return bundleDocs(
    'Gobbos — STAGE Lore (Synthesized Setting & Factions)',
    'Contains all synthesized setting lore, world-building, and factions from LORE/01_STAGE_Lore. Dev brainstorms are excluded.',
    docs
  );
}

function generateProdLore() {
  const docs = scanDirectory('LORE/03_PROD_Lore');
  return bundleDocs(
    'Gobbos — PROD Lore (Official Canon)',
    'Contains the official, locked canon lore from LORE/03_PROD_Lore.',
    docs
  );
}

function generateAllLore() {
  const prodDocs = scanDirectory('LORE/03_PROD_Lore');
  const stageDocs = scanDirectory('LORE/01_STAGE_Lore');
  return bundleDocs(
    'Gobbos — Lore Master (PROD Canon + STAGE Lore)',
    'Comprehensive compilation of all locked PROD canon followed by active STAGE lore drafts.',
    [...prodDocs, ...stageDocs]
  );
}

function generateMasterAll() {
  const prodRules = scanDirectory('02_PROD_Core_Rules');
  const stageRules = scanDirectory('01_STAGE_Drafts');
  const prodLore = scanDirectory('LORE/03_PROD_Lore');
  const stageLore = scanDirectory('LORE/01_STAGE_Lore');

  return bundleDocs(
    'Gobbos — Complete Master Compilation (Rules & Lore)',
    'Full consolidated single-file bundle containing all PROD and STAGE rules and lore. Excludes DEV brainstorms.',
    [...prodRules, ...stageRules, ...prodLore, ...stageLore]
  );
}

const markdownIt = require('markdown-it');
const md = markdownIt({ html: true, linkify: true, typographer: true });

function wrapInHtml(title, markdownContent) {
  const rendered = md.render(markdownContent);
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      color: #1a1a1a;
      background: #ffffff;
      max-width: 960px;
      margin: 0 auto;
      padding: 24px;
    }
    h1, h2, h3, h4, h5, h6 {
      color: #111;
      margin-top: 1.5em;
      margin-bottom: 0.5em;
      line-height: 1.25;
    }
    h1 { border-bottom: 2px solid #eaeaea; padding-bottom: 0.3em; font-size: 2em; }
    h2 { border-bottom: 1px solid #eaeaea; padding-bottom: 0.3em; font-size: 1.5em; }
    p, ul, ol { margin: 1em 0; }
    li { margin: 0.3em 0; }
    table {
      border-collapse: collapse;
      width: 100%;
      margin: 1.5em 0;
    }
    th, td {
      border: 1px solid #d0d7de;
      padding: 8px 12px;
      text-align: left;
    }
    th {
      background-color: #f6f8fa;
      font-weight: 600;
    }
    tr:nth-child(2n) {
      background-color: #fbfcfd;
    }
    code {
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      font-size: 0.9em;
      background: #f6f8fa;
      padding: 0.2em 0.4em;
      border-radius: 4px;
    }
    pre {
      background: #f6f8fa;
      padding: 16px;
      border-radius: 6px;
      overflow-x: auto;
      line-height: 1.45;
    }
    pre code {
      background: transparent;
      padding: 0;
    }
    blockquote {
      margin: 1em 0;
      padding: 0 1em;
      color: #57606a;
      border-left: 4px solid #d0d7de;
    }
    hr {
      height: 2px;
      padding: 0;
      margin: 24px 0;
      background-color: #d0d7de;
      border: 0;
    }
    a { color: #0969da; text-decoration: none; }
    a:hover { text-decoration: underline; }
    pre.mermaid, .mermaid {
      background: #fbfcfd;
      border: 1px solid #d0d7de;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
      margin: 1.5em 0;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <main>
    ${rendered}
  </main>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    (function() {
      mermaid.initialize({
        startOnLoad: false,
        theme: 'base',
        themeVariables: {
          fontFamily: "'Alegreya', 'Lora', Georgia, serif",
          fontSize: '14.5px',
          primaryColor: '#f0e6d6',
          primaryTextColor: '#231c16',
          primaryBorderColor: '#8c2d19',
          lineColor: '#c68a35',
          secondaryColor: '#fdfbf7',
          tertiaryColor: '#e5dcce',
          edgeLabelBackground: '#faf5ec',
          nodeBorder: '#8c2d19',
          clusterBkg: '#eee5d5',
          clusterBorder: '#c68a35'
        },
        flowchart: {
          curve: 'basis',
          padding: 16,
          nodeSpacing: 50,
          rankSpacing: 40,
          htmlLabels: true
        },
        securityLevel: 'loose'
      });
      const codeBlocks = document.querySelectorAll('pre > code.language-mermaid');
      codeBlocks.forEach(code => {
        const pre = code.parentElement;
        if (pre) {
          pre.className = 'mermaid';
          pre.textContent = code.textContent;
        }
      });
      if (document.querySelectorAll('.mermaid').length > 0) {
        mermaid.run({ nodes: document.querySelectorAll('.mermaid') });
      }
    })();
  </script>
</body>
</html>`;
}

function generateStageRulesHtml() {
  return wrapInHtml('Gobbos — STAGE Rules (Drafts & Playtest Mechanics)', generateStageRules());
}

function generateProdRulesHtml() {
  return wrapInHtml('Gobbos — PROD Core Rules (Official Locked Rules)', generateProdRules());
}

function generateAllRulesHtml() {
  return wrapInHtml('Gobbos — Rules Master (PROD Core + STAGE Drafts)', generateAllRules());
}

function generateStageLoreHtml() {
  return wrapInHtml('Gobbos — STAGE Lore (Synthesized Setting & Factions)', generateStageLore());
}

function generateProdLoreHtml() {
  return wrapInHtml('Gobbos — PROD Lore (Official Canon)', generateProdLore());
}

function generateAllLoreHtml() {
  return wrapInHtml('Gobbos — Lore Master (PROD Canon + STAGE Lore)', generateAllLore());
}

function generateMasterAllHtml() {
  return wrapInHtml('Gobbos — Complete Master Compilation (Rules & Lore)', generateMasterAll());
}

function generateLlmsTxt() {
  return `# Gobbos TTRPG — LLM Documentation Index

> Gobbos is a fast, fun, and chaotic goblin-themed tabletop skirmish RPG.
> This file indexes consolidated, continuous files optimized for Large Language Models (LLMs) and agents.
> Available in both clean semantic HTML (recommended for web chat/Gemini) and raw Markdown (.md).

## HTML Master Bundles (Recommended for Gemini / Browsers)
- [All Rules & Lore (Master)](/all_llm.html): Complete single HTML document containing all PROD and STAGE rules and lore.
- [All Rules (PROD + STAGE)](/rules_all_llm.html): Combined rules document covering official and stage mechanics.
- [All Lore (PROD + STAGE)](/lore_all_llm.html): Combined lore document covering canon and stage lore.
- [STAGE Rules](/rules_stage_llm.html): Working rules, character creation, combat, mobs, base building, and magic.
- [PROD Rules](/rules_prod_llm.html): Locked, official core rulebook.
- [STAGE Lore](/lore_stage_llm.html): Setting lore, factions, economy, and technology.
- [PROD Lore](/lore_prod_llm.html): Locked canon world lore.

## Raw Markdown Bundles (.md)
- [All Rules & Lore (Master)](/all_llm.md)
- [All Rules (PROD + STAGE)](/rules_all_llm.md)
- [All Lore (PROD + STAGE)](/lore_all_llm.md)
- [STAGE Rules](/rules_stage_llm.md)
- [PROD Rules](/rules_prod_llm.md)
- [STAGE Lore](/lore_stage_llm.md)
- [PROD Lore](/lore_prod_llm.md)

## System Reference
- Target Face Check standard: \`[Stat] [Target Face]+/[Required Successes]\`
- Core Attributes: Tough, Slink, Mouth, Brains. Hit points: Grit (Player) / Health Dice (Mob).
`;
}

module.exports = {
  scanDirectory,
  bundleDocs,
  wrapInHtml,
  generateStageRules,
  generateProdRules,
  generateAllRules,
  generateStageLore,
  generateProdLore,
  generateAllLore,
  generateMasterAll,
  generateStageRulesHtml,
  generateProdRulesHtml,
  generateAllRulesHtml,
  generateStageLoreHtml,
  generateProdLoreHtml,
  generateAllLoreHtml,
  generateMasterAllHtml,
  generateLlmsTxt
};
