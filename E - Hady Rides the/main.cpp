#include<bits/stdc++.h>
using namespace std;
int main()
{
    	
    long long n,row,col;
    cin>>n;
    row=n/4;
    if (row%2==0)
        col=n%4;
    else
        col=3-(n%4);
    cout<<row<<" "<<col<<endl;

}