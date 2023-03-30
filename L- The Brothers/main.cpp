#include <iostream>

using namespace std;

int main(){
    int i=0;
	string arr[2];
	string fName = "",pname="";
	for (; i < size(arr); i++)
	{
		cin >> fName>> pname;
		arr[i] = pname;
		
	}
	if (arr[0] == arr[1]) {
		cout << "ARE Brothers" << endl;
	}
	else
		cout << "NOT" << endl;
		
	return 0;
}