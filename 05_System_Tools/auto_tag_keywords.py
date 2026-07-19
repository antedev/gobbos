import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(REPO_ROOT, "01_STAGE_Drafts", "00_Rules", "06_Keywords Index.md")
DIRS_TO_SCAN = [
    os.path.join(REPO_ROOT, "01_STAGE_Drafts"),
    os.path.join(REPO_ROOT, "02_PROD_Core_Rules")
]

# Highly specific, non-generic single-word terms that are safe to auto-tag
SAFE_SINGLE_WORDS = {
    "bangaranga", "overclock", "taming", "shenanigan", "shenanigans", 
    "infamy", "fumbled", "farkle", "mutiny", "oddity", "oddities", 
    "blueprint", "blueprints", "loitering"
}

def load_keywords():
    keywords = set()
    if not os.path.exists(INDEX_PATH):
        print(f"Error: Index file not found at {INDEX_PATH}")
        return []
        
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    for line in lines:
        match_wiki = re.search(r'^\s*\*\s+\[\[([^\]|]+)', line)
        if match_wiki:
            term = match_wiki.group(1).strip()
            if term.startswith('['):
                term = term[1:].strip()
            if term.endswith(']'):
                term = term[:-1].strip()
            
            # Keep if it is multi-word (contains space) OR in our safe list
            if ' ' in term or term.lower() in SAFE_SINGLE_WORDS:
                keywords.add(term)
                
        match_bold = re.search(r'^\s*\*\s+\*\*\[?([^\]*:]+)\]?\*\*:', line)
        if match_bold:
            term = match_bold.group(1).strip()
            if ' ' in term or term.lower() in SAFE_SINGLE_WORDS:
                keywords.add(term)
                
    # Sort from longest to shortest
    sorted_keywords = sorted(list(keywords), key=len, reverse=True)
    return sorted_keywords

def tag_segment(text, keywords):
    pieces = [text]
    for kw in keywords:
        pattern = re.compile(r'\b(' + re.escape(kw) + r')\b', re.IGNORECASE)
        new_pieces = []
        for piece in pieces:
            if piece.startswith('[['):
                new_pieces.append(piece)
                continue
                
            parts = []
            last_idx = 0
            for match in pattern.finditer(piece):
                start, end = match.span()
                parts.append(piece[last_idx:start])
                parts.append(f"[[{match.group(1)}]]")
                last_idx = end
            parts.append(piece[last_idx:])
            new_pieces.extend([p for p in parts if p != ''])
        pieces = new_pieces
    return ''.join(pieces)

def process_file(file_path, keywords):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    lines = content.split('\n')
    new_lines = []
    
    in_code_block = False
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
            
        if in_code_block or stripped.startswith('#') or (stripped.startswith('|') and stripped.endswith('|')) or not stripped:
            new_lines.append(line)
            continue
            
        protected_pattern = re.compile(r'(\`[^\`]+\`|\[\[[^\]]+\]\]|!\[[^\]]*\]\([^\)]+\)|\[[^\]]*\]\([^\)]+\)|\[[A-Z][a-zA-Z]*\])')
        parts = protected_pattern.split(line)
        
        for i in range(len(parts)):
            if i % 2 == 0:
                parts[i] = tag_segment(parts[i], keywords)
                
        new_lines.append(''.join(parts))
        
    new_content = '\n'.join(new_lines)
    if new_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def auto_tag_keywords():
    keywords = load_keywords()
    print(f"Loaded {len(keywords)} safe keywords for auto-tagging.")
    if not keywords:
        return
        
    updated_files = 0
    for directory in DIRS_TO_SCAN:
        if not os.path.exists(directory):
            continue
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.md'):
                    file_path = os.path.join(root, file)
                    if os.path.abspath(file_path) == os.path.abspath(INDEX_PATH):
                        continue
                    if process_file(file_path, keywords):
                        print(f"Auto-tagged keywords in: {os.path.relpath(file_path, REPO_ROOT)}")
                        updated_files += 1
                        
    print(f"Finished auto-tagging. Updated {updated_files} files.")

if __name__ == "__main__":
    auto_tag_keywords()
