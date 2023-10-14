function concatenateArrays(arrA, arrB) {
    return arrB.concat(arrA);
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (N) => {
    N = parseInt(N);

    rl.question('', (inputA) => {
        const arrA = inputA.split(' ').map(Number);

        rl.question('', (inputB) => {
            const arrB = inputB.split(' ').map(Number);

            if (arrA.length !== N || arrB.length !== N) {
                rl.close();
                return;
            }

            const result = concatenateArrays(arrA, arrB);
            console.log(result.join(' '));

            rl.close();
        });
    });
});
