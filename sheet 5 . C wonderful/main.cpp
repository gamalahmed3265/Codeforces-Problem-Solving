#include <iostream>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

// Function to check if a number is odd
bool isOdd(int N) {
    return N % 2 == 1;
}

// Function to check if a binary representation is a palindrome
bool isPalindromeBinary(int N) {
    string binaryStr = bitset<32>(N).to_string();  // Assumes a 32-bit integer
    binaryStr = binaryStr.substr(binaryStr.find('1'));  // Remove leading zeroes
    string reversedStr = binaryStr;
    reverse(reversedStr.begin(), reversedStr.end());
    return binaryStr == reversedStr;
}

int main() {
    int N;
    cin >> N;

        if (isOdd(N) && isPalindromeBinary(N)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
  

    return 0;
}
