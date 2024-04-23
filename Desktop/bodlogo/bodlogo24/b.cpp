#include<iostream>
using namespace std;

#define ll long long


int main(){
	ll n,k;
	cin >> n >> k;
	
	ll a[n + 1];
	
	ll t;
	ll r = 0;
	ll mx = -1000000;
	for(int i=1; i<=n; i++){
		cin >> t;
		
		if (mx > t) r = mx + t;
		mx = max(mx, t);
	}
	
	if (r <= k) 
	cout <<"Yes";
	else 
	cout << "No";
	
	return 0;
}
