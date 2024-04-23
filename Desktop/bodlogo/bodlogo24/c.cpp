#include<iostream>
using namespace std;
#define ll long long 

int main(){
    
    ll A,B,C,D;
    cin >>A>>B>>C>>D;
    ll count=0;
    
    for(ll i=1; i*i<=B; ++i)  {
        ll y_min = max(A/i , i);
        ll y_max = min(B/i , (ll)(1e9));
        for(ll j = i; j <= B; ++j){
            ll S = i*j;
            ll P = 2*(i+j);
            if(S >=A && S <= B && P >= C && P <= D){
                count++;
            }
        }
    }
    cout << count << endl;
    
    return 0;
}
