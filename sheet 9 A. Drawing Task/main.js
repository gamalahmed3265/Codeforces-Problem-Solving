var input = readline().split` `.map(x => +x)
var n = input[0], m = input[1], k = input[2]
var grid = []
for (var i = 0; i < n; i++) {
    grid.push(".".repeat(m).split``)
}
while (k--) {
    var input = readline().split` `
    var r1 = +input[0] - 1, c1 = +input[1] - 1, r2 = +input[2] - 1, c2 = +input[3] - 1;
    var startI = Math.min(r1, r2),
        endI = Math.max(r1, r2),
        startJ = Math.min(c1, c2),
        endJ = Math.max(c1, c2),
        c = input[4]

    for (var i = startI; i <= endI; i++) {
        for (var j = startJ; j <= endJ; j++) {
            grid[i][j] = c
        }
    }

}


for (var i = 0; i < n; i++) {
    print(grid[i].join``)
}