function printNumbersFrom1ToN(N) {
    for (let i = 1; i <= N; i++) {
        process.stdout.write(i.toString());
        if (i < N) {
            process.stdout.write(" ");
        }
    }
    process.stdout.write("\n");
}

// Read input from standard input
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const N = parseInt(input);

        printNumbersFrom1ToN(N);

    rl.close();
});
