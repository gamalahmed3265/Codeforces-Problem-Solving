#include <iostream>

using namespace std;

int main(){
    int i=0,sum=0;
	long long arr[2];
	for (; i < 2; i++){
		cin >> arr[i];
	
		sum += arr[i] % 10;
	}
	cout << sum << endl;
    return 0;
}