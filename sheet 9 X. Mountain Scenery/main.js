var input = readline().split` `.map(x => +x)
var n = input[0], k = input[1]
var points = readline().split` `.map(x => +x)

while (k) {
    for (var i = 1; i < n * 2 && k; i += 2) {
        if (points[i] > points[i - 1] && points[i] > points[i + 1]) {
            if (points[i] - 1 > points[i - 1] && points[i] - 1 > points[i + 1]) {
                points[i]--;
                k--;
            }
        }
    }
}

print(...points)