const iterations = 50000;

function rollDice() {
    let res = Math.floor(Math.random() * 6) + 1;
    if (res === 6) {
        return [res, ...rollDice()];
    }
    return [res];
}

function resolve(poolSize, difficulty) {
    let target = difficulty === 'Easy' ? 4 : difficulty === 'Normal' ? 5 : 6;
    let rolls = [];
    for (let i = 0; i < poolSize; i++) {
        rolls.push(...rollDice());
    }

    let successes = rolls.filter(r => r >= target).length;
    let ones = rolls.filter(r => r === 1).length;
    let netSuccesses = successes - ones;

    let fumble = ones >= 2 && successes === 0;
    let critical = netSuccesses >= 4;

    return { rolls, successes, ones, netSuccesses, fumble, critical, target };
}

function simulate(poolSize, difficulty) {
    let statsBase = { succ: 0, fumble: 0, crit: 0 };
    let statsAdd = { succ: 0, fumble: 0, crit: 0 };
    let statsReroll = { succ: 0, fumble: 0, crit: 0 };

    for (let i = 0; i < iterations; i++) {
        // Base
        let b = resolve(poolSize, difficulty);
        if (b.successes > 0) statsBase.succ++;
        if (b.fumble) statsBase.fumble++;
        if (b.critical) statsBase.crit++;

        // Add Die
        let a = resolve(poolSize + 1, difficulty);
        if (a.successes > 0) statsAdd.succ++;
        if (a.fumble) statsAdd.fumble++;
        if (a.critical) statsAdd.crit++;

        // Reroll Ones
        let rolls = [...b.rolls];
        let initialOnes = b.ones;
        rolls = rolls.filter(r => r !== 1);
        for (let j = 0; j < initialOnes; j++) {
            rolls.push(...rollDice());
        }

        let target = b.target;
        let successes = rolls.filter(r => r >= target).length;
        let ones = rolls.filter(r => r === 1).length;
        let netSuccesses = successes - ones;

        let fumble = ones >= 2 && successes === 0;
        let critical = netSuccesses >= 4;

        if (successes > 0) statsReroll.succ++;
        if (fumble) statsReroll.fumble++;
        if (critical) statsReroll.crit++;
    }

    const pct = val => (val / iterations * 100).toFixed(1) + '%';

    console.log(`Pool: ${poolSize} (${difficulty})`);
    console.log(`  Base   -> Succ: ${pct(statsBase.succ).padStart(6)}, Fumble: ${pct(statsBase.fumble).padStart(6)}, Crit: ${pct(statsBase.crit).padStart(6)}`);
    console.log(`  +1 Die -> Succ: ${pct(statsAdd.succ).padStart(6)}, Fumble: ${pct(statsAdd.fumble).padStart(6)}, Crit: ${pct(statsAdd.crit).padStart(6)}`);
    console.log(`  Reroll -> Succ: ${pct(statsReroll.succ).padStart(6)}, Fumble: ${pct(statsReroll.fumble).padStart(6)}, Crit: ${pct(statsReroll.crit).padStart(6)}`);
    console.log('');
}

for (let d of ['Easy', 'Normal', 'Hard']) {
    for (let p of [1, 2, 3, 5]) {
        simulate(p, d);
    }
}
