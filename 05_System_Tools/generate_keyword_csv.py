import os
import re
import csv

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(REPO_ROOT, "01_STAGE_Drafts", "00_Rules", "06_Keywords Index.md")
DIRS_TO_SCAN = [
    os.path.join(REPO_ROOT, "01_STAGE_Drafts"),
    os.path.join(REPO_ROOT, "02_PROD_Core_Rules")
]
CSV_OUTPUT_PATH = os.path.join(REPO_ROOT, "05_System_Tools", "keyword_review.csv")

def load_existing_choices():
    choices = {}
    if os.path.exists(CSV_OUTPUT_PATH):
        try:
            with open(CSV_OUTPUT_PATH, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    kw = row["Keyword"].strip().lower()
                    status = row["Keep (YES/NO/REMOVE)"].strip()
                    choices[kw] = status
        except Exception as e:
            print(f"Warning: Could not read existing choices from CSV: {e}")
    return choices

def parse_defined_keywords():
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

def scan_for_wikilinks(defined_keywords, existing_choices):
    wiki_terms = {}
    wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    
    for directory in DIRS_TO_SCAN:
        if not os.path.exists(directory):
            continue
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.md'):
                    file_path = os.path.join(root, file)
                    # Skip Keywords Index itself to avoid parsing definitions as mentions
                    if os.path.abspath(file_path) == os.path.abspath(INDEX_PATH):
                        continue
                        
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    matches = wikilink_pattern.findall(content)
                    for match in matches:
                        term = match.split('|')[0].strip()
                        if term.startswith('['):
                            term = term[1:].strip()
                        if term.endswith(']'):
                            term = term[:-1].strip()
                            
                        slug = term.lower()
                        if not slug:
                            continue
                            
                        if slug not in wiki_terms:
                            in_index = "YES" if slug in defined_keywords else "NO"
                            
                            # Preserve user's existing choice if present, otherwise default
                            if slug in existing_choices:
                                keep = existing_choices[slug]
                            else:
                                keep = "YES" if in_index == "YES" else "PENDING"
                                
                            wiki_terms[slug] = {
                                "Keyword": term,
                                "Count": 0,
                                "In_Index": in_index,
                                "Keep (YES/NO/REMOVE)": keep,
                                "Files": set()
                            }
                            
                        wiki_terms[slug]["Count"] += 1
                        rel_path = os.path.relpath(file_path, REPO_ROOT).replace('\\', '/')
                        wiki_terms[slug]["Files"].add(rel_path)
                            
    return wiki_terms

def write_csv(wiki_terms):
    sorted_terms = sorted(wiki_terms.values(), key=lambda x: (x["In_Index"], -x["Count"]))
    
    with open(CSV_OUTPUT_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Keyword", "Keep (YES/NO/REMOVE)", "In_Index", "Count", "Files"])
        for term_data in sorted_terms:
            writer.writerow([
                term_data["Keyword"],
                term_data["Keep (YES/NO/REMOVE)"],
                term_data["In_Index"],
                term_data["Count"],
                ", ".join(sorted(list(term_data["Files"])))
            ])
            
    print(f"Generated review CSV with {len(sorted_terms)} unique terms at: {CSV_OUTPUT_PATH}")

if __name__ == "__main__":
    existing = load_existing_choices()
    defined = parse_defined_keywords()
    print(f"Parsed {len(defined)} defined keywords. Loaded {len(existing)} existing choices.")
    terms = scan_for_wikilinks(defined, existing)
    write_csv(terms)
