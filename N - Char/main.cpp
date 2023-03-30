#include <iostream>

using namespace std;

int main(){
    
    char c,re;
	cin >> c;
	if (c>=97 && c<=122) {
		re = c - 32;
		cout << re << endl;
	}
	else if (c >= 65 && c <= 90) {
		re = c + 32;
		cout << re << endl;
	}
		
	return 0;
}