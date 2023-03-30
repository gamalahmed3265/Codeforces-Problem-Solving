#include <iostream>

using namespace std;

int main(){
    int i=0;
	int arr[3];
	
	for (; i < 3; i++)
	{
		cin >> arr[i];
	}
	long long minNum= arr[0],maxNum = arr[0];
	for (i=1; i < 3; i++)
	{
		if (arr[i] > maxNum)
			maxNum = arr[i];
		else if (arr[i] < minNum)
			minNum = arr[i];
	}
	cout << minNum << " " << maxNum;
		
	return 0;
}