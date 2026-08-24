import os
import re
import sys
from pathlib import Path

PROD_DIR = Path(r"c:\Users\ante\Documents\github\gobbos\02_PROD_Core_Rules")

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
    "12_Adversaries_and_Threats.md",
]

def check_file_existence():
    print("=== 1. FILE EXISTENCE & ORDER CHECK ===")
    missing = []
    for ch in CHAPTERS:
        p = PROD_DIR / ch
        if not p.exists():
            missing.append(ch)
        else:
            print(f"[OK] Found {ch} ({p.stat().st_size} bytes)")
    if missing:
        print(f"[FAIL] Missing files: {missing}")
    return missing

def audit_header_hierarchy(filename, content):
    lines = content.splitlines()
    errors = []
    current_level = 0
    h1_count = 0
    
    for idx, line in enumerate(lines, 1):
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))
            header_text = match.group(2)
            if level == 1:
                h1_count += 1
            if current_level > 0 and level > current_level + 1:
                errors.append((idx, f"Header skip from H{current_level} to H{level}: '{line}'"))
            current_level = level
            
    if h1_count == 0:
        errors.append((0, "No H1 header found in file"))
    elif h1_count > 1:
        errors.append((0, f"Multiple H1 headers found ({h1_count})"))
        
    return errors

def audit_slash_notation(filename, content):
    lines = content.splitlines()
    issues = []
    
    # Check for "6+" in check notation or rules
    # Look for patterns like Brains 6+, 6+/..., or target face 6+
    # Note: 6+ can be a regular number in some non-dice contexts or invalid dice notation
    for idx, line in enumerate(lines, 1):
        # Find explicit 6+ in slash notation like 6+/1, 6+/2, etc.
        six_plus_slash = re.findall(r'(?:\w+\s+)?6\+/\d+', line)
        if six_plus_slash:
            issues.append((idx, f"Invalid '6+' in slash notation: {six_plus_slash}", line))
            
        # Find 6+ preceded by stat or check keywords
        six_plus_stat = re.findall(r'(?:Tough|Slink|Mouth|Brains|Grunt|TN|Target Number|Difficulty)\s*[:=]?\s*6\+', line, re.IGNORECASE)
        if six_plus_stat:
            issues.append((idx, f"Invalid '6+' with stat/difficulty: {six_plus_stat}", line))
            
        # Look for missing plus on 4 or 5 in slash notation, e.g. Brains 4/2, Slink 5/1
        # Valid stats: Tough, Slink, Mouth, Brains, Grunt
        missing_plus = re.findall(r'\b(Tough|Slink|Mouth|Brains|Grunt)\s+([45])/\d+\b', line)
        if missing_plus:
            issues.append((idx, f"Missing '+' on face 4 or 5 in slash notation: {missing_plus}", line))

        # Check for malformed slash notation like `Stat 4+` missing `/TN` when specifying a check
        # We can search for `[Stat] [Face]+` without `/` if intended as check
    return issues

def audit_degendering(filename, content):
    lines = content.splitlines()
    pronoun_pattern = re.compile(r'\b(he|she|they|him|her|them|his|hers|their|theirs|himself|herself|themselves)\b', re.IGNORECASE)
    findings = []
    
    in_code_block = False
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
            
        # Look for pronouns
        matches = list(pronoun_pattern.finditer(line))
        if matches:
            words = [m.group(0) for m in matches]
            findings.append((idx, words, line))
            
    return findings

def audit_keywords(filename, content):
    lines = content.splitlines()
    findings = []
    
    # 1. Squad / Unit / Swarm used for player Mob
    # Allowed exceptions: "Enemy Swarm", "Swarm Terror", "Group Attack", "Swarm Attack"
    squad_pattern = re.compile(r'\b(squad|squads)\b', re.IGNORECASE)
    unit_pattern = re.compile(r'\b(unit|units)\b', re.IGNORECASE)
    
    # 2. Health on Boss / PC (Boss should have Grit, Mob has Health / Health Dice, Enemy Bosses have Wounds)
    boss_health_pattern = re.compile(r'\b(?:Boss|PC|Goblin Boss|Player)\b[^\.\n]*\b(?:Health|Hit Points|HP)\b', re.IGNORECASE)
    
    # 3. Grit on Mob
    mob_grit_pattern = re.compile(r'\b(?:Mob|Mobs|Runts)\b[^\.\n]*\b(?:Grit)\b', re.IGNORECASE)
    
    # 4. Generic treasure instead of Loot / Loot Value
    treasure_pattern = re.compile(r'\b(treasure|gold coins|gold pieces|currency)\b', re.IGNORECASE)
    
    for idx, line in enumerate(lines, 1):
        squad_m = squad_pattern.findall(line)
        if squad_m:
            findings.append((idx, f"Potential synonym drift (squad): {squad_m}", line))
            
        unit_m = unit_pattern.findall(line)
        if unit_m:
            findings.append((idx, f"Potential synonym drift (unit): {unit_m}", line))
            
        boss_hp_m = boss_health_pattern.findall(line)
        if boss_hp_m:
            findings.append((idx, f"Potential Boss Health drift: {boss_hp_m}", line))
            
        mob_grit_m = mob_grit_pattern.findall(line)
        if mob_grit_m:
            findings.append((idx, f"Potential Mob Grit drift: {mob_grit_m}", line))
            
        treasure_m = treasure_pattern.findall(line)
        if treasure_m:
            findings.append((idx, f"Potential treasure keyword drift: {treasure_m}", line))
            
    return findings

def audit_extension_and_gaps(filename, content):
    extension_points = re.findall(r'\[CONTENT EXTENSION POINT:[^\]]+\]', content)
    missing_gaps = re.findall(r'\[MISSING RULE / GAP:[^\]]+\]', content)
    return extension_points, missing_gaps

def run_all_audits():
    check_file_existence()
    
    total_header_errors = 0
    total_slash_issues = 0
    total_pronouns = 0
    total_keyword_findings = 0
    
    print("\n" + "="*50)
    print("STARTING COMPREHENSIVE CHAPTER AUDIT")
    print("="*50)
    
    for ch in CHAPTERS:
        p = PROD_DIR / ch
        if not p.exists():
            continue
        content = p.read_text(encoding="utf-8")
        
        print(f"\n>>> AUDITING: {ch} <<<")
        
        # 1. Header Hierarchy
        h_errors = audit_header_hierarchy(ch, content)
        if h_errors:
            print(f"  [HEADER ERRORS]: {len(h_errors)}")
            for idx, msg in h_errors:
                print(f"    Line {idx}: {msg}")
            total_header_errors += len(h_errors)
        else:
            print("  [HEADER HIERARCHY]: PASS (Strict hierarchy maintained)")
            
        # 2. Slash Notation
        s_issues = audit_slash_notation(ch, content)
        if s_issues:
            print(f"  [SLASH NOTATION ISSUES]: {len(s_issues)}")
            for idx, msg, line in s_issues:
                print(f"    Line {idx}: {msg} | Snippet: {line.strip()[:80]}")
            total_slash_issues += len(s_issues)
        else:
            print("  [SLASH NOTATION]: PASS (No 6+, proper notation)")
            
        # 3. De-gendering
        pronouns = audit_degendering(ch, content)
        if pronouns:
            print(f"  [DE-GENDERING FINDINGS]: {len(pronouns)} lines with pronouns")
            for idx, words, line in pronouns:
                print(f"    Line {idx}: {words} | Snippet: {line.strip()[:80]}")
            total_pronouns += len(pronouns)
        else:
            print("  [DE-GENDERING]: PASS (100% de-gendered / second person / imperative nouns)")
            
        # 4. Keyword Constancy
        kw_findings = audit_keywords(ch, content)
        if kw_findings:
            print(f"  [KEYWORD FINDINGS]: {len(kw_findings)}")
            for idx, msg, line in kw_findings:
                print(f"    Line {idx}: {msg} | Snippet: {line.strip()[:80]}")
            total_keyword_findings += len(kw_findings)
        else:
            print("  [KEYWORD CONSTANCY]: PASS")
            
        # 5. Extension Points & Gaps
        exts, gaps = audit_extension_and_gaps(ch, content)
        print(f"  [EXTENSION POINTS]: {len(exts)} found")
        for ext in exts:
            print(f"    - {ext}")
        print(f"  [MISSING RULE GAPS]: {len(gaps)} found")
        for gap in gaps:
            print(f"    - {gap[:100]}...")

    print("\n" + "="*50)
    print("AUDIT SUMMARY TOTALS:")
    print(f"Header Errors: {total_header_errors}")
    print(f"Slash Notation Issues: {total_slash_issues}")
    print(f"De-gendering Pronoun Lines: {total_pronouns}")
    print(f"Keyword Constancy Findings: {total_keyword_findings}")
    print("="*50)

if __name__ == "__main__":
    run_all_audits()
