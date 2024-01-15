function areLinesParallel(X1, Y1, X2, Y2, X3, Y3, X4, Y4) {
    m1=(Y2-Y1)*(X4-X3)
    m2=(Y4-Y3)*(X2-X1)
    
    return m1==m2
}

// Example usage:
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (line1) => {
    rl.question('', (line2) => {
        const [X1, Y1, X2, Y2] = line1.split(' ').map(Number);
        const [X3, Y3, X4, Y4] = line2.split(' ').map(Number);

        const result = areLinesParallel(X1, Y1, X2, Y2, X3, Y3, X4, Y4);
        console.log(result ? 'YES' : 'NO');

        rl.close();
    });
});
