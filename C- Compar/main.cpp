#include <iostream>
#include <string>

using namespace std;

string lexicographical_order(string x, string y) {
  // Compare the two strings character by character.
  for (int i = 0; i < min(x.length(), y.length()); i++) {
    if (x[i] < y[i]) {
      return x;
    } else if (x[i] > y[i]) {
      return y;
    }
  }

  // If the strings are equal up to this point, then the smaller string is the one
  // with the shorter length.
  return x.length() < y.length() ? x : y;
}

int main() {
  // Read two strings from the user.
  string x, y;
  cin >> x >> y;

  // Print the smallest lexicographical string.
  cout << lexicographical_order(x, y) << endl;

  return 0;
}
