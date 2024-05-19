var input = readline().split` `.map(x => +x)
var q = input[0], icecream = input[1];
var left = 0

while (q--) {
    var input = readline().split` `
    var option = input[0], amount = +input[1];
    switch (option) {
        case '+':
            icecream += amount;
            break;
        case '-':
            if (icecream >= amount) {
                icecream -= amount
            } else {
                left++;
            }
    }
}
print(`${icecream} ${left}`)