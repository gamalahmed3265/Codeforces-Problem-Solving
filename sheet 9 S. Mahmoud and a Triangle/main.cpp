#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string canFormTriangle(int n, vector<int>& segments) {
    sort(segments.begin(), segments.end()); // Sort the segment lengths in non-decreasing order
    for (int i = 0; i < n - 2; i++) {
        if (segments[i] + segments[i + 1] > segments[i + 2]) {
            return "YES"; // If any triplet satisfies the condition, return "YES"
        }
    }
    return "NO"; // If no triplet satisfies the condition, return "NO"
}

int main() {
    int n;
    cin >> n;
    vector<int> segments(n);
    for (int i = 0; i < n; i++) {
        cin >> segments[i];
    }
    cout << canFormTriangle(n, segments) << endl;
    return 0;
}
