#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define _ ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int main()
{_
    int n, m, q;  cin >> n >> m >> q;

    int arr[n][m];
    for(int i=0 ; i<n ; i++)
        for(int j=0 ; j<m ; j++) cin >> arr[i][j];

    int rows[n], columns[m];
    for(int i=0 ; i<n ; i++) rows[i] = i;
    for(int i=0 ; i<m ; i++) columns[i] = i;

    char ch;  int a, b;  
    while(q--) {
        cin >> ch >> a >> b;   a--, b--;

        if(ch == 'r') 
            swap(rows[a], rows[b]);
        else if(ch == 'c') 
            swap(columns[a], columns[b]);
        else 
            cout << arr[rows[a]][columns[b]] << '\n';
    }
}
