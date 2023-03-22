#include <iostream>
using namespace std;

 
int main()
{
    int n;
    cin>>n;
    int arr[n];
    long long sum=0;
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
        sum+=arr[i];
    }
    if(sum<0)cout<<sum*-1<<endl;
    else cout<<sum<<endl;
 
    return 0;
}