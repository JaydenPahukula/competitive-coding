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

vector<vi> edges;
set<int> marked;

pii dfs(int curr, int parent){
    pii best = {INT_MIN, -1};
    if (marked.count(curr)) best = {0, curr};
    int s = edges[curr].size();
    rep(i, 0, s){
        if (edges[curr][i] == parent) continue;
        pii result = dfs(edges[curr][i], curr);
        best = max(best, result);
    }
    if (best.F != INT_MIN) best.F++;
    return best;
}


int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int t; cin>>t;
    rep(_, 0, t){
        int n,k; cin>>n>>k;
        marked.clear();edges.clear();
        int a;
        rep(_, 0, k){
            cin>>a;
            marked.insert(a-1);
        }
        edges = vector<vi>(n);
        int b;
        rep(_, 0, n-1){
            cin>>a>>b;
            edges[a-1].pb(b-1);
            edges[b-1].pb(a-1);
        }

        cout << dfs(dfs(0,0).S, -1).F/2 << "\n";
    }
}