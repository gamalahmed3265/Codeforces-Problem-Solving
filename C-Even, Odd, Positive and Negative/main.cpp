#include <iostream>
using namespace std;
int main() {
    int n,i;
    cin>>n;
    int el;
    int even=0,odd=0,pos=0,nev=0;
    for(i=1; i<=n; i++){
        cin>>el;
        if(el%2==0){
             even++;
        }
        else{
            odd++;
        }
            
         if(el>0){
             pos++;
        }
         else if(el<0){
             nev++;
         }
            
    }
    cout<<"Even: "<<even<<endl;
    cout<<"Odd: "<<odd<<endl;
    cout<<"Positive: "<<pos<<endl;
    cout<<"Negative: "<<nev<<endl;
    
    return 0;
}