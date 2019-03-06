/*
 *
 *************************************************************************
 * AUTHOR : Babin Dutta                                                  *
 * Language: C++14                                                       *                                      
 *************************************************************************
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

int arr[5001][2501];
int min(int a, int b){
	return (a<b)?a:b;
}
void calc()
{
	int i,j;
	for(i=0;i<=5000;i++){
		for(j=0;j<=min(i,2500);j++){
			if(j==0 || j==i) arr[i][j]=1;
			else{
				arr[i][j] = ((arr[i-1][j-1]%(mod-1))+(arr[i-1][j]%(mod-1)))%(mod-1);
			}
		}
	}
}




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

ll modD(ll a, ll b, ll p=mod){
	a = a%p;
	ll inv = modI(b,p);
	return (inv*a)%p;
}

int main()
{
	boost;
	calc();
	int t;
	cin>>t;
	
	while(t--){
		ll n,k;
		cin>>n>>k;
		ll ar[n];
		for(ll i=0;i<n;i++){
			cin>>ar[i];
		}
		sort(ar,ar+n);
		ll ans =1;
		for(ll i=0;i<n;i++){
			ll a,b=0,c=0;
			ll n1=n-1,r1=k-1,n2=n-i-1,r2=k-1,n3=i,r3=k-1;
			
			if(n1>=r1) {
				if(r1>n1/2) r1=n1-r1;
			    a = arr[n1][r1];
			}
			
			if(n2>=r2) {
				if(r2>n2/2) r2 = n2-r2;
				b = arr[n2][r2];
			}
			
			if(n3>=r3) {
				if(r3>n3/2) r3 = n3-r3;
				c = arr[n3][r3];
			} 
			ll x = ar[i];
			ll a1= power(x,a,mod);
			ll a2= power(x,((b+c)%(mod-1)),mod);
			ans = ((ans%mod)*(modD(a1,a2,mod)%mod))%mod;
		}
		cout<<ans<<endl;
	}
	return 0;
}
