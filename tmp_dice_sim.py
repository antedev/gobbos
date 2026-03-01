import random

def simulate(pool_size, difficulty='Normal', num_trials=100000):
    success_target = {'Easy': 4, 'Normal': 5, 'Hard': 6}[difficulty]
    
    def roll_dice():
        res = random.randint(1, 6)
        if res == 6:
            return [res] + roll_dice()
        return [res]
        
    def resolve(dice_pool_size):
        rolls = []
        for _ in range(dice_pool_size):
            rolls.extend(roll_dice())
        
        successes = sum(1 for r in rolls if r >= success_target)
        ones = sum(1 for r in rolls if r == 1)
        
        # Does 1 cancel success normally? Let's assume net_successes = successes - ones for criticals
        # The rules say "after you deducted any 1s, you have achived a critical success!"
        net_successes = successes - ones
        fumble = (ones >= 2 and successes == 0)
        critical = (net_successes >= 4)
        
        return successes, ones, fumble, critical
        
    def sim_base():
        s, o, f, c = resolve(pool_size)
        return s >= 1, f, c
        
    def sim_add_dice():
        s, o, f, c = resolve(pool_size + 1)
        return s >= 1, f, c
        
    def sim_reroll_ones():
        # roll base pool
        rolls = []
        for _ in range(pool_size):
            rolls.extend(roll_dice())
            
        # reroll ones (any number of ones)
        initial_ones = sum(1 for r in rolls if r == 1)
        # remove initial ones
        rolls = [r for r in rolls if r != 1]
        
        # for each 1, roll anew
        for _ in range(initial_ones):
            rolls.extend(roll_dice())
            
        successes = sum(1 for r in rolls if r >= success_target)
        ones = sum(1 for r in rolls if r == 1)
        net_successes = successes - ones
        
        fumble = (ones >= 2 and successes == 0)
        critical = (net_successes >= 4)
        
        return successes >= 1, fumble, critical

    stats_base = {'succ': 0, 'fumble': 0, 'crit': 0}
    stats_add = {'succ': 0, 'fumble': 0, 'crit': 0}
    stats_reroll = {'succ': 0, 'fumble': 0, 'crit': 0}
    
    for _ in range(num_trials):
        s, f, c = sim_base()
        stats_base['succ'] += s; stats_base['fumble'] += f; stats_base['crit'] += c
        
        s, f, c = sim_add_dice()
        stats_add['succ'] += s; stats_add['fumble'] += f; stats_add['crit'] += c
        
        s, f, c = sim_reroll_ones()
        stats_reroll['succ'] += s; stats_reroll['fumble'] += f; stats_reroll['crit'] += c
        
    def pct(val): return f"{val/num_trials*100:.1f}%"
    
    print(f"Pool: {pool_size} ({difficulty})")
    print(f"  Base   -> Succ: {pct(stats_base['succ'])}, Fumble: {pct(stats_base['fumble'])}, Crit: {pct(stats_base['crit'])}")
    print(f"  +1 Die -> Succ: {pct(stats_add['succ'])}, Fumble: {pct(stats_add['fumble'])}, Crit: {pct(stats_add['crit'])}")
    print(f"  Reroll -> Succ: {pct(stats_reroll['succ'])}, Fumble: {pct(stats_reroll['fumble'])}, Crit: {pct(stats_reroll['crit'])}")
    print()

for d in ['Easy', 'Normal', 'Hard']:
    for p in [1, 2, 3, 5]:
        simulate(p, d, 50000)
