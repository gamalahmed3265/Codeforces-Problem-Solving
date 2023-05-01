#include <bits/stdc++.h>
#define ll            long long
#define pb            push_back
#define ld            long double
#define sz            size()
#define foo(i,a,b)    for (ll i=a;i<b;i++)
#define pll           pair<ll,ll>
#define ed            "\n"
#define ct            cout
#define m_p           make_pair
#define vi            vector<ll>
#define vpll           vector<pll>
#define ff            first
#define ss            second
#define mod           1000000007

// https://codeforces.com/problemset/problem/1578/E
using namespace std;

void bahut_tezz()
{
    std::ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}


void jai_bajrangbali()
{
    ll k,n,m,x,y,cnt=0,res=0,mx=1;
    ll sum=0;
    bool ash=false;
    string s;

    cin>>n>>k;
    //ll a[n];

    ll total = pow(2,n) - 1;

    vi v;

    for(ll i=0;i<n;i++)
    {
        x = pow(2,i);
        v.pb(x);
    }

    for(ll i=0;i<n;i++)
    {
        if(k < v[i])
        {
            break;
        }
        else
        {
            cnt++;
            sum += v[i];
        }
    }


    total = total - sum;



    y = total/k;

    if(total%k)y++;

    ct<<y+cnt<<ed;

}

int main()
{
    bahut_tezz();
    long long t=1;
    cin>>t;
    while(t--)jai_bajrangbali();

    return 0;
}
