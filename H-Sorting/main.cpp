#include <iostream>
using namespace std;

void print(int arr[], int size) {
	for (int i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}
void hSelect(int arr[], int size) {
	for (int i = 0; i < size - 1; i++) {
		int index;
		int flag = 0;
		int myValue = arr[i];
		for (int z = i + 1; z < size; z++) {
			if (arr[z] < myValue) {
				index = z;
				myValue = arr[z];
				flag = 1;
			}
		}
		if (flag == 1) {
			int temp = arr[i];
			arr[i] = myValue;
			arr[index] = temp;
		}
	}
	print(arr, size);
}

int main()
{
	int size;
	cin>>size;
	int arr[size] ;
	for (int i = 0; i < size; i++) { // 0 1 2 3 4
		cin >> arr[i];
	}
	hSelect(arr,size);
	return 0;
}
