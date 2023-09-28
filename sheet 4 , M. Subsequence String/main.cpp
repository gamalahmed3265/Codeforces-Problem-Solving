#include <iostream>
#include <string>
using namespace std;

string findHelloSubsequence(string s) {
    string target = "hello";
    int i = 0;  // Index for the target string "hello"

    for (char c : s) {
        if (c == target[i]) {
            i++;
            if (i == target.length()) {
                return "YES";
            }
        }
    }

    return "NO";
}

int main() {
    string S;
    cin >> S;

    string result = findHelloSubsequence(S);
    cout << result << endl;

    return 0;
}
