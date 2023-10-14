#include<bits/stdc++.h>
using namespace std;
double sum(int size){
	double sum;
	for(int i=0;i<size;i++){ 
		double value;
		cin>>value;
		sum+= value;
	}
	return sum;
}
int main()
{
	int size;
	cin>>size;
	cout<<setprecision(8)<<sum(size)/size<<endl;
}