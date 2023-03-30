#include <iostream>
using namespace std;

int main(){
    
    const int n = 3;
	int arr[n];
    int odarr[n];
	for (int i = 0; i < n; i++){
	    	cin >> arr[i];
	    	odarr[i]=arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n; j++) {
			if (arr[j] > arr[i]) {
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
		
	}
	
	int e=n-1;
	while (e>=0) {
		cout << arr[e] << endl;
		e--;
		}
		cout << endl;
		for (int i = 0; i < n; i++){
		    cout << odarr[i]<<endl;
		}
	
    return 0;
}