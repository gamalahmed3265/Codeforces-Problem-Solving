// Function to check if a number is odd
function isOdd(N) {
    return N % 2 === 1;
}

// Function to check if a binary representation is a palindrome
function isPalindromeBinary(N) {
    const binaryStr = N.toString(2);
    return binaryStr === binaryStr.split('').reverse().join('');
}

// Read input from standard input
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const N = parseInt(input);

        if (isOdd(N) && isPalindromeBinary(N)) {
            console.log('YES');
        } else {
            console.log('NO');
        }

    rl.close();
});
