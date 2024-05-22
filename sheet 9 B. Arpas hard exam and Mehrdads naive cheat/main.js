var ans = {
    0: 6,
    1: 8,
    2: 4,
    3: 2,
}
var num = +readline()
print(num ? ans[num % 4] : 1)