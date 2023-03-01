#include <iostream>

using namespace std;

int main()
{
    short n,h,a,cnt=0;cin>>n>>h;
    while(n--)
    {
        cin>>a;
        if(a>h)cnt+=2;
        else cnt+=1;
    }
    cout<<cnt<<endl;
    return 0;
}