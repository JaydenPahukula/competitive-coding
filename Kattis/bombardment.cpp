#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define F first
#define S second
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int n,r;cin>>n>>r;
    vi a(n);rep(i,0,n)cin>>a[i];
    sort(all(a));
    vi ops;
    while(sz(a)){
        int j = 0;
        pii best={-1,-1};
        rep(i,0,n){
            while(j<n && a[j]<a[i]+2*r+1)j++;
            int score = j-i;
            if(score>best.F) {
                best={score,a[j-1]-r};
            }
        }
        ops.pb({best.S});
        // cout<<"kill "<<best.F<<" ending "<<best.S<<endl;
        assert(best.F>0);
        vi b;
        rep(i,0,n){
            if(a[i]<best.S-r || a[i]>best.S+r) b.pb(a[i]);
            // else cout<<"killed "<<a[i]<<endl;
        }
        a=b;
        n=sz(a);
    }
    cout<<sz(ops)<<'\n';
    for(int v : ops)cout<<v<<' ';
    cout<<'\n';
}


