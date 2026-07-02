#!/usr/bin/env node
'use strict';

const fs = require('fs-extra');
const path = require('path');
const markdownIt = require('markdown-it');
const anchor = require('markdown-it-anchor');

// ============================================================
// Configuration
// ============================================================
const REPO_ROOT = path.resolve(__dirname, '..', '..');
const DIST_DIR = path.join(__dirname, 'dist');
const TEMPLATE_PATH = path.join(__dirname, 'template.html');
const INDEX_TEMPLATE_PATH = path.join(__dirname, 'index-template.html');
const STYLE_PATH = path.join(__dirname, 'style.css');

const ENVIRONMENTS = [
  { key: 'dev',        dir: '00_DEV_Brainstorms',  title: 'DEV Rules',        subtitle: 'Raw ideas and brainstorms', icon: '💡' },
  { key: 'stage',      dir: '01_STAGE_Drafts',     title: 'STAGE Rules',      subtitle: 'Playtesting & review materials', icon: '🧪' },
  { key: 'prod',       dir: '02_PROD_Core_Rules',  title: 'PROD Rules',       subtitle: 'The official rulebook', icon: '📖' },
  { key: 'dev-lore',   dir: 'LORE/00_DEV_Lore',    title: 'DEV Lore',         subtitle: 'Volatile lore brainstorms', icon: '🔮' },
  { key: 'stage-lore', dir: 'LORE/01_STAGE_Lore',   title: 'STAGE Lore',       subtitle: 'Synthesized lore drafts',   icon: '📜' },
  { key: 'prod-lore',  dir: 'LORE/03_PROD_Lore',    title: 'PROD Lore',        subtitle: 'Locked canon',              icon: '🏛️' },
];

// ============================================================
// Helpers
// ============================================================
function stripPrefix(name) {
  return name.replace(/^\d+[_\s]+/, '').replace(/\.md$/i, '');
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

function numericSort(a, b) {
  const numA = parseInt((a.match(/^(\d+)/) || ['', '9999'])[1], 10);
  const numB = parseInt((b.match(/^(\d+)/) || ['', '9999'])[1], 10);
  if (numA !== numB) return numA - numB;
  return a.localeCompare(b);
}

function escapeHtml(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function getPageFilename(envKey, pageSlug, isFirstPage) {
  if (isFirstPage) {
    return `${envKey}.html`;
  }
  return `${envKey}--${pageSlug}.html`;
}

function resolveWikiLink(linkText, env) {
  const trimmed = linkText.trim();
  const slug = slugify(trimmed);

  // If a wikiMap is provided in the markdown-it env object, look up the target URL
  if (env && env.wikiMap && env.wikiMap.has(slug)) {
    return env.wikiMap.get(slug);
  }

  // Fallback to section/heading anchor on the current page
  return `#${slug}`;
}

// ============================================================
// Wikilinks Plugin for markdown-it
// ============================================================
function wikilinksPlugin(md) {
  const wikiRe = /\[\[([^\]]+)\]\]/g;
  const defaultTextRender = md.renderer.rules.text || function (tokens, idx) {
    return md.utils.escapeHtml(tokens[idx].content);
  };

  md.renderer.rules.text = function (tokens, idx, options, env, self) {
    const content = tokens[idx].content;
    if (!content.includes('[[')) {
      return defaultTextRender(tokens, idx, options, env, self);
    }
    return content.replace(wikiRe, (_, linkText) => {
      const trimmed = linkText.trim();
      const targetUrl = resolveWikiLink(trimmed, env);
      return `<a href="${targetUrl}" class="wikilink" title="${escapeHtml(trimmed)}">${escapeHtml(trimmed)}</a>`;
    });
  };
}

// ============================================================
// Markdown Parser Setup
// ============================================================
function createMarkdownParser() {
  const md = markdownIt({ html: true, linkify: true, typographer: true });

  md.use(anchor, {
    permalink: false,
    slugify: slugify,
    uniqueSlugStartIndex: 1,
  });

  md.use(wikilinksPlugin);
  return md;
}

// ============================================================
// Content Scanner
// ============================================================
function scanEnvironment(envDirName) {
  const envPath = path.join(REPO_ROOT, envDirName);
  if (!fs.existsSync(envPath)) return { sections: [], hasContent: false };

  const entries = fs.readdirSync(envPath, { withFileTypes: true });
  const sections = [];

  const subdirs = entries
    .filter(e => e.isDirectory() && !e.name.startsWith('.'))
    .map(e => e.name).sort(numericSort);

  const looseFiles = entries
    .filter(e => e.isFile() && e.name.toLowerCase().endsWith('.md'))
    .map(e => e.name).sort(numericSort);

  // Subdirectories → folder sections with child pages
  for (const dir of subdirs) {
    const sectionName = stripPrefix(dir);
    const sectionSlug = slugify(sectionName);
    const dirPath = path.join(envPath, dir);
    const mdFiles = fs.readdirSync(dirPath)
      .filter(f => f.toLowerCase().endsWith('.md'))
      .sort(numericSort);

    const pages = mdFiles.map(file => ({
      name: stripPrefix(file),
      slug: `${sectionSlug}--${slugify(stripPrefix(file))}`,
      content: fs.readFileSync(path.join(dirPath, file), 'utf-8'),
    }));

    if (pages.length > 0) {
      sections.push({ name: sectionName, slug: sectionSlug, pages, isFolder: true });
    }
  }

  // Loose files → standalone sections
  for (const file of looseFiles) {
    const pageName = stripPrefix(file);
    const pageSlug = slugify(pageName);
    sections.push({
      name: pageName,
      slug: pageSlug,
      pages: [{ name: pageName, slug: pageSlug, content: fs.readFileSync(path.join(envPath, file), 'utf-8') }],
      isFolder: false,
    });
  }

  return { sections, hasContent: sections.length > 0 };
}

// ============================================================
// Build sidebar navigation HTML
// ============================================================
function buildSidebarNav(sections, envKey, firstPageSlug, currentPageSlug) {
  let nav = '';

  for (const section of sections) {
    if (section.isFolder) {
      const isCurrentSection = section.pages.some(p => p.slug === currentPageSlug);
      const expandedAttr = isCurrentSection ? 'aria-expanded="true"' : 'aria-expanded="false"';
      const displayStyle = isCurrentSection ? '' : 'style="display: none;"';

      nav += `<div class="nav-group">`;
      nav += `<button class="nav-group-toggle" ${expandedAttr} data-target="${section.slug}">`;
      nav += `<span class="toggle-icon">${isCurrentSection ? '▾' : '▸'}</span>${escapeHtml(section.name)}</button>`;
      nav += `<ul class="nav-pages" id="nav-${section.slug}" ${displayStyle}>`;
      
      for (const page of section.pages) {
        const isFirst = page.slug === firstPageSlug;
        const pageUrl = getPageFilename(envKey, page.slug, isFirst);
        const isActive = page.slug === currentPageSlug;
        const activeClass = isActive ? ' nav-link--active' : '';
        
        nav += `<li><a href="${pageUrl}" class="nav-link${activeClass}" data-target="${page.slug}">${escapeHtml(page.name)}</a></li>`;
      }
      nav += `</ul></div>`;
    } else {
      const page = section.pages[0];
      const isFirst = page.slug === firstPageSlug;
      const pageUrl = getPageFilename(envKey, page.slug, isFirst);
      const isActive = page.slug === currentPageSlug;
      const activeClass = isActive ? ' nav-link--active' : '';

      nav += `<div class="nav-group nav-group--solo">`;
      nav += `<a href="${pageUrl}" class="nav-link nav-link--solo${activeClass}" data-target="${page.slug}">${escapeHtml(section.name)}</a>`;
      nav += `</div>`;
    }
  }

  return nav;
}

// ============================================================
// Build environment navigation tabs
// ============================================================
function buildEnvNav(activeKey) {
  return ENVIRONMENTS.map(env => {
    const cls = env.key === activeKey ? 'env-tab env-tab--active' : 'env-tab';
    const href = env.key === 'index' ? 'index.html' : `${env.key}.html`;
    return `<a href="${href}" class="${cls}">${env.icon} ${env.title}</a>`;
  }).join('\n');
}

// ============================================================
// Main Build
// ============================================================
async function build() {
  console.log('🔨 Building Gobbos Rulebook & Lore Site (Multi-Page Agent-Friendly)...\n');

  // Ensure dist exists and is clean
  await fs.emptyDir(DIST_DIR);

  // Read templates
  const template = await fs.readFile(TEMPLATE_PATH, 'utf-8');
  const indexTemplate = await fs.readFile(INDEX_TEMPLATE_PATH, 'utf-8');

  // Copy CSS
  await fs.copy(STYLE_PATH, path.join(DIST_DIR, 'style.css'));
  console.log('  ✅ Copied style.css');

  // Create markdown parser
  const md = createMarkdownParser();

  // Build each environment page
  for (const env of ENVIRONMENTS) {
    const { sections, hasContent } = scanEnvironment(env.dir);

    if (!hasContent) {
      // Empty state page (e.g. stage.html or prod.html when empty)
      const mainContent = `<div class="empty-state"><h2>No content yet</h2><p>Rules will appear here once they are added to <code>${env.dir}/</code>.</p></div>`;
      const sidebarNav = '<p class="nav-empty">No sections yet</p>';
      
      const html = template
        .replace(/\{\{TITLE\}\}/g, `${env.title} — Gobbos`)
        .replace(/\{\{PAGE_TITLE\}\}/g, env.title)
        .replace(/\{\{SUBTITLE\}\}/g, env.subtitle)
        .replace('{{NAV_CONTENT}}', sidebarNav)
        .replace('{{MAIN_CONTENT}}', mainContent)
        .replace('{{ENV_NAV}}', buildEnvNav(env.key));

      await fs.writeFile(path.join(DIST_DIR, `${env.key}.html`), html, 'utf-8');
      console.log(`  ✅ Built ${env.key}.html (Empty State)`);
      continue;
    }

    // Determine the first page's slug to map it to env.key.html
    let firstPageSlug = null;
    if (sections.length > 0 && sections[0].pages.length > 0) {
      firstPageSlug = sections[0].pages[0].slug;
    }

    // Build the wikiMap for wikilinks lookup
    const wikiMap = new Map();
    for (const section of sections) {
      for (const page of section.pages) {
        const isFirst = page.slug === firstPageSlug;
        const pageUrl = getPageFilename(env.key, page.slug, isFirst);
        wikiMap.set(page.slug, pageUrl);
        wikiMap.set(slugify(page.name), pageUrl);
      }
      if (section.pages.length > 0) {
        const isFirst = section.pages[0].slug === firstPageSlug;
        const sectionUrl = getPageFilename(env.key, section.pages[0].slug, isFirst);
        wikiMap.set(slugify(section.name), sectionUrl);
      }
    }

    // Build a separate page for each page in every section
    let pagesCount = 0;
    for (const section of sections) {
      for (const page of section.pages) {
        const isFirst = page.slug === firstPageSlug;
        const pageFilename = getPageFilename(env.key, page.slug, isFirst);
        
        const mainContent = md.render(page.content, { wikiMap });
        const sidebarNav = buildSidebarNav(sections, env.key, firstPageSlug, page.slug);

        const html = template
          .replace(/\{\{TITLE\}\}/g, `${page.name} — ${env.title} — Gobbos`)
          .replace(/\{\{PAGE_TITLE\}\}/g, env.title)
          .replace(/\{\{SUBTITLE\}\}/g, env.subtitle)
          .replace('{{NAV_CONTENT}}', sidebarNav)
          .replace('{{MAIN_CONTENT}}', mainContent)
          .replace('{{ENV_NAV}}', buildEnvNav(env.key));

        await fs.writeFile(path.join(DIST_DIR, pageFilename), html, 'utf-8');
        pagesCount++;
      }
    }
    
    console.log(`  ✅ Built environment ${env.key} (${sections.length} sections, ${pagesCount} pages)`);
  }

  // Build index page
  const envCards = ENVIRONMENTS.map(env => {
    const { hasContent } = scanEnvironment(env.dir);
    const statusClass = hasContent ? 'card--active' : 'card--empty';
    const statusText = hasContent ? 'Has content' : 'Empty';
    return `<a href="${env.key}.html" class="env-card ${statusClass}">
      <span class="env-card-icon">${env.icon}</span>
      <h2>${escapeHtml(env.title)}</h2>
      <p>${escapeHtml(env.subtitle)}</p>
      <span class="env-card-status">${statusText}</span>
    </a>`;
  }).join('\n');

  const indexHtml = indexTemplate.replace('{{ENV_CARDS}}', envCards);
  await fs.writeFile(path.join(DIST_DIR, 'index.html'), indexHtml, 'utf-8');
  console.log('  ✅ Built index.html\n');

  // Write success status.json
  const statusData = {
    status: 'success',
    timestamp: new Date().toISOString()
  };
  await fs.writeJson(path.join(DIST_DIR, 'status.json'), statusData, { spaces: 2 });
  console.log('  ✅ Written status.json (success)\n');

  console.log('🎉 Build complete! Files in:', DIST_DIR);
}

build().catch(err => {
  console.error('❌ Build failed:', err);
  process.exit(1);
});
