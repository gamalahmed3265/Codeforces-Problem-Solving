const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to check if a string is a palindrome
function isPalindrome(s) {
    // Remove non-alphanumeric characters and convert to lowercase
    s = s.replace(/[^a-z]/g, "").toLowerCase();

    // Reverse the string
    const reversed = s.split("").reverse().join("");

    // Check if the original and reversed strings are the same
    return s === reversed;
}

// Ask the user to enter a string
rl.question('', (userInput) => {
    if (isPalindrome(userInput)) {
        console.log("YES");
    } else {
        console.log("NO");
    }

    rl.close();
});
