Project Overview:
We shall make a small webpage to display the rules of the game. The rules are written in Markdown (.md) files and organized into a specific directory structure (e.g., 01_STAGE_Drafts, 02_PROD_Core_Rules, 00_DEV_Brainstorms). Inside these root folders are subfolders (e.g., 00_Rules, 01_Characters & Mobs) which contain numbered markdown files (e.g., 00_Overview.md, 01_Dice.md).

The Goal:
Create a lightweight Node.js build script that converts these folders into a beautifully styled, readable web documentation site. I do not want a heavy framework (No React, Vue, etc.). The output should be pure, static HTML/CSS/JS files that can run locally but are ready to be deployed to a custom domain later.

Core Architecture Requirements:

Single-Page Per Environment: I do NOT want each .md file to be a separate HTML page. Instead, create one long, continuous HTML page for each main root directory (e.g., stage.html, prod.html, dev.html).

Concatenation & Sorting: The build script must read the subfolders and files sequentially (respecting their numbered prefixes like 01_..., 02_...) and concatenate their Markdown content into one massive string per environment before converting it to HTML.

Sidebar Navigation (Table of Contents): Generate a sticky left-hand sidebar menu based on the folder and file names. Clicking a link in the menu should simply scroll the user down the long page to the corresponding section (using #id anchor tags).

Clean File Names in UI: Strip the numbered prefixes and .md extensions for the UI rendering (e.g., 01_Characters & Mobs/10_Stats.md should just read "Characters & Mobs" as a header and "Stats" as a link).

Future-Proofing (Wikilinks):
I eventually want to use Obsidian-style wikilinks ([[Page Name]]). Please configure the Markdown parser to recognize this syntax. For now, it just needs to generate an anchor link #page-name that targets the corresponding header ID on the same long page.

Tech Stack Recommendations:

Build Environment: Node.js.

Markdown Parsing: markdown-it (because it's highly extensible).

Plugins: markdown-it-anchor (to automatically generate IDs for headers so the menu can link to them) and a plugin or custom regex to handle [[wikilinks]].

Styling: Vanilla CSS. Use CSS variables for easy theming.

To-Do List for the AI Agent (Step-by-Step Implementation):

Setup: Initialize a basic Node project (package.json) and install necessary dependencies (markdown-it, markdown-it-anchor, fs-extra).

File System Logic: Write a script (build.js) that traverses the specific root directories (Dev, Stage, Prod).

Content Parsing: For each root directory, loop through its subdirectories sequentially, read every .md file, and combine them.

Anchor Generation: As the files are read, inject the file's name (stripped of numbers) as an <h2> or <h1> header if it isn't already, so the Markdown parser can assign an ID to it.

Menu Generation: Build a hierarchical JSON object or HTML string representing the folder structure to be injected into the sidebar navigation.

Template Engine: Create a basic HTML template (template.html) with a <nav> for the sidebar and a <main> for the content. Inject the parsed HTML and Menu into this template.

Styling (CSS): Write a clean, readable CSS file. Requirements:

Sticky sidebar on the left (250px wide), main content on the right.

Max-width on the main content (e.g., 800px or 65ch) for optimal readability.

Nice typography (sans-serif for UI, serif for reading text).

Slightly warm, "TTRPG manual" aesthetic (off-white/cream background for the text, distinct blockquotes, styled tables).

Output: Save the final files (index.html, stage.html, prod.html, style.css) into a /dist or /public folder.

Dev Server: Add a simple script to package.json to run the build and serve the /dist folder locally.