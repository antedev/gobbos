import os
import re
import csv

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(REPO_ROOT, "01_STAGE_Drafts", "00_Rules", "06_Keywords Index.md")
CSV_PATH = os.path.join(REPO_ROOT, "05_System_Tools", "keyword_review.csv")
DIRS_TO_SCAN = [
    os.path.join(REPO_ROOT, "01_STAGE_Drafts"),
    os.path.join(REPO_ROOT, "02_PROD_Core_Rules")
]

def load_base_keywords():
    base_keywords = {} # lowercase -> original case
    
    # 1. Load from Keywords Index
    if os.path.exists(INDEX_PATH):
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
                base_keywords[term.lower()] = term

    # 2. Load from CSV (if user set Keep = YES)
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                keyword = row["Keyword"].strip()
                keep = row["Keep (YES/NO/REMOVE)"].strip().upper()
                if keep == "YES":
                    base_keywords[keyword.lower()] = keyword

    # Ensure absolute defaults are in there
    defaults = ["mob", "tag", "trait", "wound", "quirk", "twist", "zone", "bane", "boon", "stat"]
    for d in defaults:
        if d not in base_keywords:
            base_keywords[d] = d.capitalize()

    return base_keywords

def get_singular_candidate(term):
    t = term.strip()
    # Strip possessive 's
    if t.lower().endswith("'s"):
        t = t[:-2]
    # Strip possessive apostrophe (e.g. Mobs' -> Mobs)
    if t.endswith("'"):
        t = t[:-1]
    # Strip plural es (e.g. Successes -> Success)
    if t.lower().endswith("es"):
        t = t[:-2]
    # Strip plural s (e.g. Mobs -> Mob), avoiding words ending in ss like Boss or Class
    elif t.lower().endswith("s") and not t.lower().endswith("ss"):
        t = t[:-1]
    return t

def consolidate_links():
    bases = load_base_keywords()
    print(f"Loaded {len(bases)} base keywords for consolidation.")
    
    updated_files_count = 0
    total_consolidations = 0

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
                    def replace_plural_link(match):
                        nonlocal total_consolidations
                        full_match = match.group(0)
                        inner = match.group(1).strip()
                        parts = inner.split('|')
                        target = parts[0].strip()
                        display = parts[1].strip() if len(parts) > 1 else target

                        # Clean tags brackets if present in target
                        clean_target = target
                        is_tag = False
                        if clean_target.startswith('[') and clean_target.endswith(']'):
                            clean_target = clean_target[1:-1].strip()
                            is_tag = True

                        target_lower = clean_target.lower()

                        # Check if a singular candidate matches a base keyword, and is different from target
                        cand = get_singular_candidate(clean_target)
                        cand_lower = cand.lower()
                        
                        if cand_lower != target_lower and cand_lower in bases:
                            base_word = bases[cand_lower]
                            new_target = f"[{base_word}]" if is_tag else base_word
                            total_consolidations += 1
                            print(f"Consolidating: [[{inner}]] -> [[{new_target}|{display}]]")
                            return f"[[{new_target}|{display}]]"

                        return full_match

                    # Replace matches
                    content = re.sub(r'\[\[([^\]]+)\]\]', replace_plural_link, content)

                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated_files_count += 1

    print(f"Consolidation complete: Made {total_consolidations} updates across {updated_files_count} files.")

if __name__ == "__main__":
    consolidate_links()
