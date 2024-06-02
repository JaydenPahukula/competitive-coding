#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define F first
#define S second
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int SZ = 5000001;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int n;cin>>n;
    vi dp(SZ,INT_MAX);
    dp[0] = 0;
    rep(i,0,n){
        int a,b;cin>>a>>b;
        vi newdp(SZ,INT_MAX);
        for(int j = SZ-1; j > -1; --j){
            if (dp[j] == INT_MAX) continue;
            if (j+a < SZ) newdp[j+a] = min(newdp[j+a], dp[j]);
            newdp[j] = min(newdp[j], dp[j]+b);
        }
        rep(i,0,SZ) dp[i] = newdp[i];
    }
    int mn = INT_MAX;
    rep(i,0,SZ) mn = min(mn, max(i,dp[i]));
    cout << mn << endl;
}
