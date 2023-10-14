#include<bits/stdc++.h>
using namespace std;
void printNumber(int a){
	for(int i=1;i<=a;i++){
		if (i!=a)
		{
		cout<<i<<" ";
		}
		else{

		cout<<i;
		}
		
	}
}
int main(){
	
	int a;
	cin>>a;
	printNumber(a);
	
}