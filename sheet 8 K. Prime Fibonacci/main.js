

var sequence = [0, 1];
var prime = [0, 0, 0]
function generateFibonacciSequence() {
    for (var i = 2; i <= 51; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
        prime.push(isPrime(sequence[i]));
    }
}
function isPrime(num) {
    if (num <= 1) {
        return 0
    }
    for (var i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return 0;
        }
    }
    return 1;
}
generateFibonacciSequence()

var test = readline()
while (test--) {
    var number = +  readline()
    print(prime[number] ? "prime" : "not prime")
}