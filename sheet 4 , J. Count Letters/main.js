const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function countLetters(a){
    let char_count={};
    let cr;

    for (let index = 0; index < a.length; index++) {
        if (a[index] in char_count) {
            
            char_count[a[index]]+=1;
        }
        else{
            char_count[a[index]]=1;

        }
    }
    counter_sorted=Object.keys(char_count).sort()

    for (let index = 0; index < counter_sorted.length; index++) {
        console.log(`${counter_sorted[index]} : ${char_count[counter_sorted[index]]}`);
    }    

}


// Ask the user to enter a string
rl.question('', (userInput) => {
    countLetters(userInput)

    rl.close();
});
