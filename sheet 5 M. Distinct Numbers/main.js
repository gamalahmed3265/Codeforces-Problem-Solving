const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const s = 1000;

function countNumber(arr, size) {
    let count = 1;
    for (let i = 1; i < size; i++) {
        if (arr[i] !== arr[i - 1]) {
            count++;
        }
    }
    return count;
}

function main() {
    rl.question('', (size) => {
        size = parseInt(size);

        if (size === 0) {
            console.log(0);
            rl.close();
            return;
        }

        const arr = new Array(s);

        rl.question('', (input) => {
            const inputArr = input.split(' ').map(Number);

            for (let i = 0; i < size; i++) {
                arr[i] = inputArr[i];
            }

            arr.length = size;
            arr.sort((a, b) => a - b);

            console.log(countNumber(arr, size));
            rl.close();
        });
    });
}

main();
