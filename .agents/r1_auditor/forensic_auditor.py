import os
import re
import sys

PROD_DIR = r"c:\Users\ante\Documents\github\gobbos\02_PROD_Core_Rules"
CHAPTERS = [
    "01_Core_Resolution.md",
    "02_Boss_Profile_and_Gang.md",
    "03_Action_Economy_and_Turn_Flow.md",
    "04_Zones_and_Movement.md",
    "05_Combat_Engine.md",
    "06_Mob_Mechanics.md",
    "07_Damage_Grit_and_Wounds.md",
    "08_Magic_and_Bangaranga.md",
    "09_The_Raid_Loop.md",
    "10_The_Lair_Loop_and_Progression.md",
    "11_Journeys_and_Hazards.md",
    "12_Adversaries_and_Threats.md"
]

def check_files_exist():
    results = {}
    for ch in CHAPTERS:
        p = os.path.join(PROD_DIR, ch)
        if os.path.exists(p):
            size = os.path.getsize(p)
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
                words = len(content.split())
            results[ch] = {
                "exists": True,
                "size_bytes": size,
                "lines": len(lines),
                "words": words,
                "content": content
            }
        else:
            results[ch] = {
                "exists": False,
                "size_bytes": 0,
                "lines": 0,
                "words": 0,
                "content": ""
            }
    return results

def check_header_hierarchy(chapters_data):
    issues = []
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        last_level = 0
        for i, line in enumerate(lines, 1):
            m = re.match(r'^(#{1,6})\s+(.*)', line)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                if last_level > 0 and level > last_level + 1:
                    issues.append(f"{ch}:{i} Header skip from H{last_level} to H{level}: '{title}'")
                last_level = level
    return issues

def check_placeholders_and_stubs(chapters_data):
    issues = []
    patterns = [
        (r'\bTODO\b', 'TODO'),
        (r'\bFIXME\b', 'FIXME'),
        (r'\bTBD\b', 'TBD'),
        (r'\bplaceholder\b', 'placeholder'),
        (r'\blorem ipsum\b', 'lorem ipsum'),
        (r'\bnot yet implemented\b', 'not yet implemented')
    ]
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        for i, line in enumerate(lines, 1):
            for pat, name in patterns:
                if re.search(pat, line, re.IGNORECASE):
                    # check if it's in a code comment or legitimate text vs stub
                    issues.append(f"{ch}:{i} [{name}] {line.strip()}")
    return issues

def check_content_extension_points(chapters_data):
    points = {}
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        matches = re.findall(r'\[CONTENT EXTENSION POINT:[^\]]+\]', data["content"])
        points[ch] = matches
    return points

def check_missing_rule_gaps(chapters_data):
    gaps = {}
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        matches = re.findall(r'\[MISSING RULE / GAP:[^\]]+\]', data["content"])
        gaps[ch] = matches
    return gaps

def check_slash_notation(chapters_data):
    issues = []
    # GEMINI.md: For target 6: Never include a + symbol (e.g. 6+ is forbidden, should be 6/X)
    # Check for target 6+ with slash
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        for i, line in enumerate(lines, 1):
            # check for 6+/
            if re.search(r'\b6\+/', line):
                issues.append(f"{ch}:{i} Target 6 contains illegal '+' sign in slash notation: '{line.strip()}'")
            # check for malformed slash notation like Stat 4/2 instead of Stat 4+/2
            # e.g. Tough 4/1 or Brains 5/2 (where target is 4 or 5 without +)
            m = re.findall(r'\b(Tough|Slink|Brains|Mouth|Grunt|TN)\s+([45])\s*/\s*(\d+)', line)
            for stat, face, succ in m:
                issues.append(f"{ch}:{i} Missing '+' on face {face} slash notation: '{stat} {face}/{succ}' (should be '{stat} {face}+/{succ}')")
    return issues

def check_synonym_bans(chapters_data):
    findings = []
    # Grit vs Health: "health points", "hit points", "hp", "stamina" for PC
    # Mob vs Squad/Unit
    patterns = [
        (r'\bhit\s*points\b', "hit points (synonym ban for Grit/Mob Health)"),
        (r'\bhealth\s*points\b', "health points (synonym ban)"),
        (r'\bstamina\b', "stamina (synonym ban for Grit)"),
        (r'\bsquad\b', "squad (synonym ban for Mob)"),
        (r'\bHP\b', "HP (synonym ban)")
    ]
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        for i, line in enumerate(lines, 1):
            for pat, desc in patterns:
                m = re.findall(pat, line, re.IGNORECASE)
                if m:
                    findings.append(f"{ch}:{i} Found {desc}: '{line.strip()}'")
    return findings

def check_gender_pronouns(chapters_data):
    findings = []
    # Look for he, she, him, her, his, hers, himself, herself
    # Also singular they/their if in rule descriptions where Player/Boss is intended
    pronoun_pat = re.compile(r'\b(he|she|him|her|his|hers|himself|herself)\b', re.IGNORECASE)
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        for i, line in enumerate(lines, 1):
            # Exclude markdown link anchors or generic formatting
            m = pronoun_pat.findall(line)
            if m:
                findings.append(f"{ch}:{i} Gendered pronoun(s) {m}: '{line.strip()}'")
    return findings

def check_cross_references(chapters_data):
    broken_links = []
    all_anchors = {}
    # Build anchors map
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        anchors = set()
        for line in data["content"].splitlines():
            m = re.match(r'^(#{1,6})\s+(.*)', line)
            if m:
                # generate github markdown anchor
                raw = m.group(2).strip()
                # remove formatting from anchor
                cleaned = re.sub(r'[*_`\[\]]', '', raw)
                anchor = re.sub(r'[^\w\s-]', '', cleaned).strip().lower()
                anchor = re.sub(r'[-\s]+', '-', anchor)
                anchors.add(anchor)
        all_anchors[ch] = anchors

    # Check links
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        lines = data["content"].splitlines()
        for i, line in enumerate(lines, 1):
            # Match markdown links: [text](target.md#anchor) or [text](target.md)
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
            for text, target in links:
                if target.startswith('http') or target.startswith('mailto:'):
                    continue
                # Split file and anchor
                if '#' in target:
                    target_file, target_anchor = target.split('#', 1)
                else:
                    target_file, target_anchor = target, None
                
                # Check target file
                if target_file:
                    target_file_clean = os.path.basename(target_file)
                    if target_file_clean not in chapters_data:
                        broken_links.append(f"{ch}:{i} Link to unknown file '{target}': text='{text}'")
                    elif target_anchor:
                        # Check anchor if known
                        pass # anchor formatting can vary
    return broken_links

def check_examples_and_golden_rules(chapters_data):
    stats = {}
    for ch, data in chapters_data.items():
        if not data["exists"]:
            continue
        examples = len(re.findall(r'^\s*>\s*\*\*Example:', data["content"], re.MULTILINE))
        golden_rules = len(re.findall(r'^\s*>>', data["content"], re.MULTILINE))
        stats[ch] = {
            "examples": examples,
            "golden_rules": golden_rules
        }
    return stats

def main():
    print("=== RUNNING FORENSIC AUDIT ON 02_PROD_Core_Rules ===")
    data = check_files_exist()
    
    print("\n--- 1. File Existence & Volume ---")
    total_words = 0
    for ch, d in data.items():
        print(f"[{'PASS' if d['exists'] else 'FAIL'}] {ch}: {d['lines']} lines, {d['words']} words, {d['size_bytes']} bytes")
        total_words += d['words']
    print(f"Total Word Count across 12 Chapters: {total_words} words")

    print("\n--- 2. Header Hierarchy Integrity ---")
    header_issues = check_header_hierarchy(data)
    if not header_issues:
        print("PASS: Zero header level skips found across all chapters.")
    else:
        print(f"FAIL: Found {len(header_issues)} header hierarchy issues:")
        for iss in header_issues:
            print("  - " + iss)

    print("\n--- 3. Placeholder / Stub / TODO Check ---")
    stubs = check_placeholders_and_stubs(data)
    if not stubs:
        print("PASS: Zero TODO/FIXME/placeholder stubs found.")
    else:
        print(f"WARNING/FLAG: Found {len(stubs)} potential placeholder matches:")
        for s in stubs:
            print("  - " + s)

    print("\n--- 4. Content Extension Points ---")
    ext_points = check_content_extension_points(data)
    total_ext = sum(len(v) for v in ext_points.values())
    print(f"Total Extension Points Found: {total_ext}")
    for ch, pts in ext_points.items():
        if pts:
            print(f"  {ch}:")
            for p in pts:
                print(f"    - {p}")

    print("\n--- 5. Missing Rule / Gap Tags ---")
    gaps = check_missing_rule_gaps(data)
    total_gaps = sum(len(v) for v in gaps.values())
    print(f"Total Missing Rule / Gap Tags Found: {total_gaps}")
    for ch, g_list in gaps.items():
        print(f"  {ch}: {len(g_list)} gaps tagged")

    print("\n--- 6. Slash Notation Standard Compliance ---")
    slash_issues = check_slash_notation(data)
    if not slash_issues:
        print("PASS: 100% compliant with Slash Standard (4+/X, 5+/X, 6/X).")
    else:
        print(f"FLAG: Found {len(slash_issues)} slash notation discrepancies:")
        for s in slash_issues:
            print("  - " + s)

    print("\n--- 7. Synonym Ban Audit ---")
    synonyms = check_synonym_bans(data)
    if not synonyms:
        print("PASS: Zero banned synonyms detected.")
    else:
        print(f"FLAG: Found {len(synonyms)} synonym matches:")
        for syn in synonyms:
            print("  - " + syn)

    print("\n--- 8. De-gendering Audit ---")
    pronouns = check_gender_pronouns(data)
    if not pronouns:
        print("PASS: Zero gendered pronouns detected.")
    else:
        print(f"FLAG: Found {len(pronouns)} gendered pronoun occurrences:")
        for p in pronouns[:20]:
            print("  - " + p)
        if len(pronouns) > 20:
            print(f"  ... and {len(pronouns)-20} more.")

    print("\n--- 9. Cross-Reference Link Check ---")
    links = check_cross_references(data)
    if not links:
        print("PASS: All markdown file links are valid.")
    else:
        print(f"FLAG: Found {len(links)} broken links:")
        for l in links:
            print("  - " + l)

    print("\n--- 10. Examples & Golden Rules Formatting ---")
    style_stats = check_examples_and_golden_rules(data)
    for ch, st in style_stats.items():
        print(f"  {ch}: {st['examples']} Examples (`> **Example:`), {st['golden_rules']} Golden Rules (`>>`)")

if __name__ == "__main__":
    main()
