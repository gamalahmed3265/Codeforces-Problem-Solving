#include <bits/stdc++.h>
#define pb push_back
#define sc1(n) scanf("%lld",&n)
#define sc2(a,b) scanf("%lld%lld",&a,&b)
#define sc3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define MX 100000
using namespace std;

typedef long long int ll;
typedef unsigned long long ul;
//ios_base::sync_with_stdio(false);
//cin.tie(NULL);
int main()
{
    map<string,ll>mp;
    map<string,string>ans;
    map<string,ll>mp2;
    ll n;
    sc1(n);
    while(n--)
    {
        string str;
        cin>>str;
        ll len=str.size();
        mp2.clear();
        for(ll i=0; i<len; i++)
        {
            string now="";
            for(ll j=i; j<len; j++)
            {
                now+=str[j];
                if(mp2.count(now)==0)
                    mp[now]++;
                mp2[now]++;
                //cout<<now<<" "<<mp[now]<<endl;
                ans[now]=str;
            }

        }
    }
    ll q;
    sc1(q);
    while(q--)
    {
        string str;
        cin>>str;
        if(mp.find(str)!=mp.end())
        {
            printf("%lld ",mp[str]);
            cout<<ans[str]<<"\n";
        }
        else
            printf("0 -\n");
    }
    return 0;
}