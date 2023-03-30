#include<bits/stdc++.h>
using namespace std;  
int main()  
{ 

	int num1;
	cin >> num1;
	(num1 / 1000 % 2 == 0) ?
		cout << "EVEN" << endl :
		cout << "ODD" << endl;
		
		return 0;
}