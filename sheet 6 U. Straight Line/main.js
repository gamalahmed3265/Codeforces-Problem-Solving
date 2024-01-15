function arePointsOnStraightLine(X1, Y1, X2, Y2, X3, Y3) {
    // Calculate slopes
    const slope1 = (Y3 - Y2) * (X2 - X1);
    const slope2 = (Y2 - Y1) * (X3 - X2);

    // Check if slopes are equal
    return slope1 === slope2;
}

// Example usage:
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (point1) => {
    rl.question('', (point2) => {
        rl.question('', (point3) => {
            const [X1, Y1] = point1.split(' ').map(Number);
            const [X2, Y2] = point2.split(' ').map(Number);
            const [X3, Y3] = point3.split(' ').map(Number);

            const result = arePointsOnStraightLine(X1, Y1, X2, Y2, X3, Y3);
            console.log(result ? 'YES' : 'NO');

            rl.close();
        });
    });
});
