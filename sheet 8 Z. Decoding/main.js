function decodePolycarpEncoding(n, s) {
    let result = "";
    let i = 0;
    
    while (n > 0) {
        if (n % 2 === 0) {
            result = s[i] + result;
        } else {
            result = result + s[i];
        }
        i++;
        n--;
    }
    
    return result;
}

// Read input
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputLines = [];
rl.on('line', (line) => {
    inputLines.push(line);
    if (inputLines.length === 2) {
        const n = parseInt(inputLines[0]);
        const s = inputLines[1];
        const decodedWord = decodePolycarpEncoding(n, s);
        console.log(decodedWord);
        rl.close();
    }
});
