#include <iostream>

using namespace std;

int main(){
    
	char c;
	cin >> c;
	if (c>=97 && c<=122) {
		cout << "ALPHA" << endl;
		cout << "IS SMALL" << endl;
	}
	else if (c >= 65 && c <= 90) {
		cout << "ALPHA" << endl;
		cout << "IS CAPITAL" << endl;
	}
	else{
		cout << "IS DIGIT" << endl;
	}
	
		
	return 0;
}