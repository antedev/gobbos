import math

def get_single_die_success_probs(difficulty='normal'):
    # Returns a list where index k is the probability of getting k successes from a single die (with explosions).
    # Since we only care about up to 10 successes, we can truncate the infinite sum.
    # P(6) = 1/6 (always 1 success + another die)
    # Easy: 4, 5 (prob 2/6) give 1 success, 1, 2, 3 (prob 3/6) give 0 successes.
    # Normal: 5 (prob 1/6) give 1 success, 1, 2, 3, 4 (prob 4/6) give 0 successes.
    # Hard: 1, 2, 3, 4, 5 (prob 5/6) give 0 successes.
    
    # We can solve the distribution of a single die S analytically or recursively.
    # S = 0 if we roll a failure:
    # Easy: 3/6, Normal: 4/6, Hard: 5/6
    # S = 1 if we roll a non-exploding success (4,5 for Easy; 5 for Normal; none for Hard) OR roll a 6 and then get 0 successes.
    # S = k (k >= 1): P(S = k) = P(non-exploding success)*P(S = k-1 | no explosion) + P(6)*P(S = k-1)
    # Actually, the recursive relation is:
    # S = (0 with prob p_fail) or (1 with prob p_succ) or (1 + S' with prob 1/6)
    # Let's compute it iteratively up to 15 successes.
    max_s = 15
    probs = [0.0] * (max_s + 1)
    
    if difficulty == 'easy':
        p_fail = 3.0 / 6.0
        p_succ = 2.0 / 6.0
    elif difficulty == 'normal':
        p_fail = 4.0 / 6.0
        p_succ = 1.0 / 6.0
    else: # hard
        p_fail = 5.0 / 6.0
        p_succ = 0.0 / 6.0
        
    probs[0] = p_fail
    # We can solve: P(S = k) = p_succ * (k==1) + 1/6 * P(S = k-1) for k >= 1.
    # Wait, is that correct?
    # If we roll 6 (prob 1/6), we get 1 success and roll again. So if the next roll gets k-1 successes, we get k successes.
    # If we roll a non-exploding success (prob p_succ), we get 1 success and stop, so this contributes to k=1.
    # If we roll a failure (prob p_fail), we get 0 successes.
    # Thus:
    # P(S = 0) = p_fail
    # P(S = 1) = p_succ + 1/6 * P(S = 0) = p_succ + 1/6 * p_fail
    # P(S = k) = 1/6 * P(S = k-1) for k >= 2.
    # Let's verify:
    # Easy: P(S=0) = 0.5; P(S=1) = 2/6 + 1/6 * 0.5 = 1/3 + 1/12 = 5/12; P(S=2) = 5/72; etc.
    # Sum: 1/2 + 5/12 * (1 + 1/6 + 1/36 + ...) = 1/2 + 5/12 * 6/5 = 1/2 + 1/2 = 1. Yes!
    probs[1] = p_succ + (1.0 / 6.0) * probs[0]
    for k in range(2, max_s + 1):
        probs[k] = (1.0 / 6.0) * probs[k-1]
        
    return probs

def get_pool_success_probs(dice_count, difficulty='normal'):
    # Convolve single die probabilities dice_count times
    single_probs = get_single_die_success_probs(difficulty)
    
    current_probs = [1.0] # 0 dice has 100% chance of 0 successes
    for _ in range(dice_count):
        next_probs = [0.0] * (len(current_probs) + len(single_probs) - 1)
        for i, p_curr in enumerate(current_probs):
            for j, p_single in enumerate(single_probs):
                next_probs[i+j] += p_curr * p_single
        current_probs = next_probs
        
    return current_probs

def get_fumble_prob(dice_count, difficulty='normal'):
    # Fumble = 0 successes and at least two physical 1s.
    # Since 0 successes means all dice rolled must be in the failure range (no 6s, so no explosions).
    # Failure range size |F|:
    # Easy: F = {1, 2, 3} (|F| = 3)
    # Normal: F = {1, 2, 3, 4} (|F| = 4)
    # Hard: F = {1, 2, 3, 4, 5} (|F| = 5)
    
    if dice_count < 2:
        return 0.0
        
    if difficulty == 'easy':
        f_size = 3
    elif difficulty == 'normal':
        f_size = 4
    else: # hard
        f_size = 5
        
    # P(all in F) = (f_size / 6)^dice_count
    # In F, each die is 1 with prob 1/f_size, and non-1 with prob (f_size-1)/f_size.
    # We want at least two 1s, which is 1 - P(zero 1s | all in F) - P(one 1 | all in F).
    # P(zero 1s | all in F) = ((f_size-1)/f_size)^dice_count
    # P(one 1 | all in F) = dice_count * (1/f_size) * ((f_size-1)/f_size)^(dice_count-1)
    
    p_all_f = (f_size / 6.0) ** dice_count
    p_zero_1_cond = ((f_size - 1.0) / f_size) ** dice_count
    p_one_1_cond = dice_count * (1.0 / f_size) * (((f_size - 1.0) / f_size) ** (dice_count - 1))
    
    p_fumble = p_all_f * (1.0 - p_zero_1_cond - p_one_1_cond)
    return p_fumble

def format_percentage(val):
    return f"{val * 100:.1f}%"

def run_analysis():
    difficulties = ['easy', 'normal', 'hard']
    
    print("# DICE PROBABILITY ANALYSIS: STAT VS. STAT + 1D")
    print("This report compares the current **Stat + 1d** mechanic against the proposed **Stat** mechanic.")
    
    for diff in difficulties:
        print(f"\n## Difficulty: {diff.upper()}")
        print("| Dice Pool | Expected Successes | Success TN:1 | Success TN:2 | Success TN:3 | Fumble Chance |")
        print("| :--- | :---: | :---: | :---: | :---: | :---: |")
        for pool in range(1, 7):
            probs = get_pool_success_probs(pool, diff)
            expected = sum(k * p for k, p in enumerate(probs))
            
            # Cumulative successes
            p_tn1 = sum(probs[k] for k in range(1, len(probs)))
            p_tn2 = sum(probs[k] for k in range(2, len(probs)))
            p_tn3 = sum(probs[k] for k in range(3, len(probs)))
            
            p_fumble = get_fumble_prob(pool, diff)
            
            print(f"| **{pool}d6** | {expected:.2f} | {format_percentage(p_tn1)} | {format_percentage(p_tn2)} | {format_percentage(p_tn3)} | {format_percentage(p_fumble)} |")

    print("\n## Impact on Core Gameplay Loop")
    
    # Let's compare Stat level (1 to 5) under both systems:
    # System A (Current): Pool = Stat + 1d (i.e., Stat 1 rolls 2d6, Stat 5 rolls 6d6)
    # System B (Proposed): Pool = Stat (i.e., Stat 1 rolls 1d6, Stat 5 rolls 5d6)
    
    print("\n### 1. Success Rate Comparison (TN:1, Normal Difficulty)")
    print("| Stat Level | Pool (Current) | Success (Current) | Pool (Proposed) | Success (Proposed) | Difference |")
    print("| :---: | :---: | :---: | :---: | :---: | :---: |")
    for stat in range(1, 6):
        probs_curr = get_pool_success_probs(stat + 1, 'normal')
        p_curr = sum(probs_curr[k] for k in range(1, len(probs_curr)))
        
        probs_prop = get_pool_success_probs(stat, 'normal')
        p_prop = sum(probs_prop[k] for k in range(1, len(probs_prop)))
        
        diff_val = p_prop - p_curr
        print(f"| **{stat}** | {stat+1}d6 | {format_percentage(p_curr)} | {stat}d6 | {format_percentage(p_prop)} | **{diff_val*100:+.1f}%** |")
        
    print("\n### 2. Fumble Rate Comparison (Normal Difficulty)")
    print("| Stat Level | Pool (Current) | Fumble (Current) | Pool (Proposed) | Fumble (Proposed) | Difference |")
    print("| :---: | :---: | :---: | :---: | :---: | :---: |")
    for stat in range(1, 6):
        f_curr = get_fumble_prob(stat + 1, 'normal')
        f_prop = get_fumble_prob(stat, 'normal')
        diff_val = f_prop - f_curr
        print(f"| **{stat}** | {stat+1}d6 | {format_percentage(f_curr)} | {stat}d6 | {format_percentage(f_prop)} | **{diff_val*100:+.1f}%** |")
        
    print("\n### 3. Combat Matchups: PC Dodge vs Enemy Attack")
    print("*Expected damage taken (Enemy Attack - Dodge Successes) when defending using Slink (Normal Difficulty)*")
    print("| Slink Level | Enemy Attack | Expected Damage (Current, Slink+1) | Expected Damage (Proposed, Slink) | Increase in Damage |")
    print("| :---: | :---: | :---: | :---: | :---: |")
    for slink in [1, 2, 3, 5]: # standard slink values (1 starting, 3 gives bonus defense, 5 is max)
        for atk in [1, 2, 3]:
            # Current pool = slink + 1
            probs_curr = get_pool_success_probs(slink + 1, 'normal')
            exp_curr = 0.0
            for k, p in enumerate(probs_curr):
                exp_curr += max(0, atk - k) * p
                
            # Proposed pool = slink
            probs_prop = get_pool_success_probs(slink, 'normal')
            exp_prop = 0.0
            for k, p in enumerate(probs_prop):
                exp_prop += max(0, atk - k) * p
                
            diff_dmg = exp_prop - exp_curr
            print(f"| Slink {slink} | Attack {atk} | {exp_curr:.2f} | {exp_prop:.2f} | **+{diff_dmg:.2f}** |")

    print("\n### 4. Combat Matchups: PC Attack vs Enemy Defence (One-Hit Kill)")
    print("*Chance to roll successes >= Defence TN to instantly kill standard enemies (Normal Difficulty)*")
    print("| Tough Level | Enemy Defence | Kill Chance (Current, Tough+1) | Kill Chance (Proposed, Tough) | Difference |")
    print("| :---: | :---: | :---: | :---: | :---: |")
    for tough in [1, 2, 3, 5]:
        for def_tn in [1, 2, 3]:
            probs_curr = get_pool_success_probs(tough + 1, 'normal')
            p_curr = sum(probs_curr[k] for k in range(def_tn, len(probs_curr)))
            
            probs_prop = get_pool_success_probs(tough, 'normal')
            p_prop = sum(probs_prop[k] for k in range(def_tn, len(probs_prop)))
            
            diff_val = p_prop - p_curr
            print(f"| Tough {tough} | Defence {def_tn} | {format_percentage(p_curr)} | {format_percentage(p_prop)} | **{diff_val*100:+.1f}%** |")

if __name__ == '__main__':
    run_analysis()
