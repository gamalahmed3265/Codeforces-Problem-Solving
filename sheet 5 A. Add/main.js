function sumNumbers(X, Y) {
    return X + Y;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const [X, Y] = input.split(' ').map(Number);

        const result = sumNumbers(X, Y);
        console.log(result);

    rl.close();
});
