/*
 *
 ********************************************************************************
 * AUTHOR : Babin Dutta                                                         *
 * Language: C++14                                                              *                                      
 ********************************************************************************
 *
 */
 
 
 
 
 
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define mod 1000000007
#define setto(n) cout << fixed << setprecision(n)
#define pb push_back
#define lb std::lower_bound
#define tstll(t) ll t; cin>>t; while(t--)
#define lfor(i,n) for(i=0;i<n;i++)
#define ft first
#define se second
typedef pair<int,int> p;
 



ll power(ll x, ll y, ll p)
{
    ll res = 1;      // Initialize result
 
    x = x % p;  // Update x if it is more than or 
                // equal to p
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;  
    }
    return res;
}
ll modInverse(ll A,ll M)
{
    return power(A,M-2,M);
}

ll modI(ll a, ll p=mod){
	ll m0=p;
	ll y=0,x=1;
	if(p==1) return 0;
	while(a>1){
		ll q = a/p;
		ll t = p;
		p = a%p, a=t;
		t = y;
		y = x- q*y;
		x=t;
	}
	if(x<0) x+= m0;
	return x;
}


 
int main() {
	#ifdef JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #endif
	boost;
    	ll n,k,p,q,ans;
    	cin>>n>>k;
    	q = power(2,n-1,mod);
    	p = q-n;
    	ll z = modI(q,mod);
    	ans = ((z%mod)*(p%mod))%mod;
    	cout<<ans<<endl;

	return 0;
} 
