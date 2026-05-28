import random
from collections import Counter

def simulate_cast(pool_size, difficulty):
    # Determine success threshold
    if difficulty == "Easy":
        success_min = 4
    elif difficulty == "Normal":
        success_min = 5
    elif difficulty == "Hard":
        success_min = 6
    else:
        raise ValueError("Invalid difficulty")
    
    # Roll dice with exploding 6s
    dice_to_roll = pool_size
    all_rolls = []
    while dice_to_roll > 0:
        rolls = [random.randint(1, 6) for _ in range(dice_to_roll)]
        all_rolls.extend(rolls)
        # Count 6s to explode
        dice_to_roll = sum(1 for r in rolls if r == 6)
        
    # Split into successes and non-successes
    successes = [r for r in all_rolls if r >= success_min]
    non_successes = [r for r in all_rolls if r < success_min]
    
    # Calculate highest success set
    if not successes:
        success_tier = 0
    else:
        success_counts = Counter(successes)
        max_success_set = max(success_counts.values())
        success_tier = min(max_success_set, 5) # Cap at T5
        
    # Calculate highest non-success set
    if not non_successes:
        side_effect_tier = 0
    else:
        non_success_counts = Counter(non_successes)
        max_non_success_set = max(non_success_counts.values())
        if max_non_success_set >= 2:
            side_effect_tier = min(max_non_success_set, 5) # Cap at T5
        else:
            side_effect_tier = 0
            
    return success_tier, side_effect_tier

def run_simulation(pool_sizes, difficulties, iterations=100000):
    results = {}
    for diff in difficulties:
        results[diff] = {}
        for size in pool_sizes:
            success_dist = Counter()
            side_effect_dist = Counter()
            for _ in range(iterations):
                s_tier, se_tier = simulate_cast(size, diff)
                success_dist[s_tier] += 1
                side_effect_dist[se_tier] += 1
                
            results[diff][size] = {
                "success": {k: v / iterations for k, v in success_dist.items()},
                "side_effect": {k: v / iterations for k, v in side_effect_dist.items()}
            }
    return results

def print_report(results, pool_sizes, difficulties):
    print("# Gobbos Magic Dice Probability Report\n")
    for diff in difficulties:
        print(f"## Difficulty: {diff}")
        print("| Pool Size | Spell Fails (T0) | T1 (Singleton) | T2 (Pair) | T3 (Triple) | T4 (Quad) | T5 (Legend) | Any Side Effect (T2+) |")
        print("|---|---|---|---|---|---|---|---|")
        for size in pool_sizes:
            s = results[diff][size]["success"]
            se = results[diff][size]["side_effect"]
            
            p_fail = s.get(0, 0.0) * 100
            p_t1 = s.get(1, 0.0) * 100
            p_t2 = s.get(2, 0.0) * 100
            p_t3 = s.get(3, 0.0) * 100
            p_t4 = s.get(4, 0.0) * 100
            p_t5 = s.get(5, 0.0) * 100
            
            # Any side effect is T2, T3, T4, T5
            p_se = sum(se.get(k, 0.0) for k in [2, 3, 4, 5]) * 100
            
            print(f"| **{size}d6** | {p_fail:.1f}% | {p_t1:.1f}% | {p_t2:.1f}% | {p_t3:.1f}% | {p_t4:.1f}% | {p_t5:.1f}% | {p_se:.1f}% |")
        print("\n")
        
        print("### Side Effect Breakdown")
        print("| Pool Size | No Side Effect | T2 Side Effect | T3 Side Effect | T4+ Side Effect |")
        print("|---|---|---|---|---|")
        for size in pool_sizes:
            se = results[diff][size]["side_effect"]
            p_no_se = se.get(0, 0.0) * 100
            p_se2 = se.get(2, 0.0) * 100
            p_se3 = se.get(3, 0.0) * 100
            p_se4plus = sum(se.get(k, 0.0) for k in [4, 5]) * 100
            print(f"| **{size}d6** | {p_no_se:.1f}% | {p_se2:.1f}% | {p_se3:.1f}% | {p_se4plus:.1f}% |")
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    pool_sizes = [3, 4, 5, 6]
    difficulties = ["Easy", "Normal", "Hard"]
    results = run_simulation(pool_sizes, difficulties)
    print_report(results, pool_sizes, difficulties)
