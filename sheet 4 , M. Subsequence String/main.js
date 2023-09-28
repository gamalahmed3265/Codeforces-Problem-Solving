const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function findHelloSubsequence(s) {
    const target = "hello";
    let i = 0;  // Index for the target string "hello"

    for (const char of s) {
        if (char === target[i]) {
            i++;
            if (i === target.length) {
                return "YES";
            }
        }
    }

    return "NO";
}

rl.question("", (S) => {
    const result = findHelloSubsequence(S.trim());
    console.log(result);
    rl.close();
});
