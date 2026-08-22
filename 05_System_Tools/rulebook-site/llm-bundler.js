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

function generateLlmsTxt() {
  return `# Gobbos TTRPG — LLM Documentation Index

> Gobbos is a fast, fun, and chaotic goblin-themed tabletop skirmish RPG.
> This file indexes consolidated, continuous Markdown files optimized for Large Language Models (LLMs) and agents.
> All files exclude noisy brainstorms and contain strictly structured STAGE and PROD material.

## Master Bundles
- [All Rules & Lore (Master)](/all_llm.md): Complete single continuous file containing all PROD and STAGE rules and lore.
- [All Rules (PROD + STAGE)](/rules_all_llm.md): Combined rules bundle covering official and stage mechanics.
- [All Lore (PROD + STAGE)](/lore_all_llm.md): Combined lore bundle covering canon and stage lore.

## Specific Rule Bundles
- [STAGE Rules](/rules_stage_llm.md): Working rules, character creation, combat, mobs, base building, and magic.
- [PROD Rules](/rules_prod_llm.md): Locked, official core rulebook files.

## Specific Lore Bundles
- [STAGE Lore](/lore_stage_llm.md): Setting lore, factions, economy, and solar ichor technology.
- [PROD Lore](/lore_prod_llm.md): Locked canon world lore.

## System Reference
- Target Face Check standard: \`[Stat] [Target Face]+/[Required Successes]\`
- Core Attributes: Tough, Slink, Mouth, Brains. Hit points: Grit (Player) / Health Dice (Mob).
`;
}

module.exports = {
  scanDirectory,
  bundleDocs,
  generateStageRules,
  generateProdRules,
  generateAllRules,
  generateStageLore,
  generateProdLore,
  generateAllLore,
  generateMasterAll,
  generateLlmsTxt
};
