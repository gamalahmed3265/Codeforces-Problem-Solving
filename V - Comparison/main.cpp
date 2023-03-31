#include<iostream>
using namespace std;
int main() {

   int num1, num2;
	char s;
	cin >> num1 >> s >> num2;
	
	switch (s) {
	case '<':
		if (num1 < num2)
			cout << "Right" << endl;
		else
			cout << "Wrong" << endl;
			break;
	case '=':
		if (num1 == num2)
			cout << "Right" << endl;
		else
			cout << "Wrong" << endl;
			break;
	case '>':
		if (num1 > num2)
			cout << "Right" << endl;
		else
			cout << "Wrong" << endl;
			break;
	}

    return 0;
}