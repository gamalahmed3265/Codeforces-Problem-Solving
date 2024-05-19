var input = readline().split` `.map(x => +x);
var rows = input[0], cols = input[1];
var cake = [];
var eatenCakes = 0;
for (var i = 0; i < rows; i++) {
    var row = readline().split``;
    cake.push(row);
    if (!row.includes("S")) {
        for (var j = 0; j < cols; j++) {
            cake[i][j] = '#';
            eatenCakes++;
        }
    }
}


for (var i = 0; i < cols; i++) {
    var col = [];
    for (var j = 0; j < rows; j++) {
        col.push(cake[j][i]);
    }
    if (!col.includes('S')) {
        for (var j = 0; j < rows; j++) {
            if (cake[j][i] === '.') {
                cake[j][i] = '#';
                eatenCakes++;
            }
        }
    }
}
print(eatenCakes);
