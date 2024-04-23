#include<iostream>
#include<cmath>
using namespace std;

#define ll long long
int main() {
    ll n,division=0;
    cin >> n;
    
    for(ll i=1; i<=sqrt(n); ++i){
        if(n % i == 0){
           division +=2;
           if(i * i == n) division--;   
        }
    }
    
    cout<<division;
    
    return 0;
}
