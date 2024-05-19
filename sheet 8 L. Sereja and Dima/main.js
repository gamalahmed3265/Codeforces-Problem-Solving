var numberOfCards = +readline()
var cards = readline().split` `.map(x => +x)
var sereja = 0, dima = 0;
var turn = true; // true = sereja, false = dima
while (cards.length) {
    if (turn) {
        if (cards[0] > cards[cards.length - 1]) {
            sereja += cards.shift()
        } else {
            sereja += cards.pop()
        }
        turn = !turn
    } else {
        if (cards[0] > cards[cards.length - 1]) {
            dima += cards.shift()
        } else {
            dima += cards.pop()
        }
        turn = !turn
    }
}
 
print(`${sereja} ${dima}`)