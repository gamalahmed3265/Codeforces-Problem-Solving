#include <iostream>

using namespace std;
#include <cmath>

int main(){
   double num1, num2;
	cin >> num1 >> num2;
	double re = num1 / num2;
	cout << "floor "<<num1<<" / " << num2 << " = "<<floor(re)<<endl;
	cout << "ceil " << num1 << " / " << num2 << " = " << ceil(re) << endl;
	cout << "round " << num1 << " / " << num2 << " = " << round(re) << endl;
	
	return 0;
}