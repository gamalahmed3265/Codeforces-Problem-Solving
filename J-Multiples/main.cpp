#include <iostream>

using namespace std;
#include <cmath>

int main(){
    int num1, num2;
	cin >> num1 >> num2;
	if (num1 % num2==0)
		cout << "Multiples" << endl;
	else if(num2 % num1 == 0)
		cout << "Multiples" << endl;
	else
		cout << "No Multiples" << endl;
		
	return 0;
}