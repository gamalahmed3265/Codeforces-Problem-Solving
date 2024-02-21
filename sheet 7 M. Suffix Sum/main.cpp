#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int arr[100000];
int n;
long long sum(int index){ 

	if(index == n){
		return 0;
	}
	
	return arr[index] + sum(index+1);
}
int main()
{
    int m;
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	cout<<sum(n-m)<<"\n";

    return 0;
}