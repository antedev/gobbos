import os
import re
import csv

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO_ROOT, "05_System_Tools", "keyword_review.csv")
INDEX_PATH = os.path.join(REPO_ROOT, "01_STAGE_Drafts", "00_Rules", "06_Keywords Index.md")
DIRS_TO_SCAN = [
    os.path.join(REPO_ROOT, "01_STAGE_Drafts"),
    os.path.join(REPO_ROOT, "02_PROD_Core_Rules")
]

def parse_existing_index_terms():
    defined = set()
    if not os.path.exists(INDEX_PATH):
        return defined
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    for line in lines:
        match_obj = re.search(r'^\s*\*\s+\[\[([^\]]+)\]\]', line)
        if match_obj:
            term = match_obj.group(1).strip()
            if term.startswith('['):
                term = term[1:].strip()
            if term.endswith(']'):
                term = term[:-1].strip()
            defined.add(term.lower())
    return defined

def apply_choices():
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV file not found at {CSV_PATH}")
        return

    # Load terms to remove and keep
    to_remove = set()
    to_add_to_index = []

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = row["Keyword"].strip()
            keep_status = row["Keep (YES/NO/REMOVE)"].strip().upper()
            in_index = row["In_Index"].strip().upper()

            if keep_status == "REMOVE" or keep_status == "NO":
                to_remove.add(keyword.lower())
            elif keep_status == "YES" and in_index == "NO":
                to_add_to_index.append(keyword)

    if not to_remove and not to_add_to_index:
        print("No actions requested.")
        return

    print(f"Terms to remove from wikilinks: {len(to_remove)} terms")
    print(f"New keywords to define in index: {len(to_add_to_index)} terms")

    # 1. Sweep files and replace [[WORD]] with **WORD** for removed terms
    if to_remove:
        for directory in DIRS_TO_SCAN:
            if not os.path.exists(directory):
                continue
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith('.md'):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        original_content = content
                        
                        # Regex matching [[Keyword]] or [[Keyword|Display]]
                        def replace_wikilink(match):
                            full_match = match.group(0)
                            inner = match.group(1).strip()
                            parts = inner.split('|')
                            term = parts[0].strip()
                            display = parts[1].strip() if len(parts) > 1 else term

                            # Handle bracketed tags inside like [[[Bonded]]]
                            clean_term = term
                            if clean_term.startswith('['):
                                clean_term = clean_term[1:]
                            if clean_term.endswith(']'):
                                clean_term = clean_term[:-1]

                            if clean_term.lower() in to_remove:
                                return f"**{display}**"
                            return full_match

                        # Replace matches
                        content = re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, content)

                        if content != original_content:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"Updated wikilinks to bold in: {os.path.relpath(file_path, REPO_ROOT)}")

    # 2. Append new keywords to the keyword index file
    if to_add_to_index and os.path.exists(INDEX_PATH):
        existing_terms = parse_existing_index_terms()
        terms_to_append = [t for t in to_add_to_index if t.lower() not in existing_terms]

        if terms_to_append:
            with open(INDEX_PATH, 'r', encoding='utf-8') as f:
                index_content = f.read()

            # Ensure newline at end
            if not index_content.endswith('\n'):
                index_content += '\n'

            # Check if ## Unsorted Keywords section exists
            section_header = "## Unsorted Keywords"
            if section_header not in index_content:
                index_content += f"\n{section_header}\n"

            for term in terms_to_append:
                index_content += f"*   [[{term}]]: [TODO: Define {term}]\n"

            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(index_content)
            print(f"Appended {len(terms_to_append)} keywords to {os.path.relpath(INDEX_PATH, REPO_ROOT)}")
        else:
            print("All new keywords are already defined in the index file.")

    print("Cleanup and indexing step complete.")

if __name__ == "__main__":
    apply_choices()
