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

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int n; cin>>n;

    vector<vi> children(n);
    rep(i,0,n-1){
        int a; cin>>a;
        children[a-1].pb(i+1);
    }

    function<bool(int)> recurse = [&](int curr){
        int leafCount = 0;
        rep(i,0,children[curr].size()){
            if (children[children[curr][i]].size()==0){
                leafCount++;
            } else {
                if (!recurse(children[curr][i])) return false;
            }
        }
        return leafCount >= 3;
    };

    cout<<(recurse(0)?"Yes":"No")<<"\n";
}