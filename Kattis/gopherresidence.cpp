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
typedef vector<double> vd;

vi topoSort(const vector<vi>& gr) {
    vi indeg(sz(gr)), ret;
    for (auto& li : gr) for (int x : li) indeg[x]++;
    queue<int> q; // use priority_queue for lexic. largest ans.
    rep(i,0,sz(gr)) if (indeg[i] == 0) q.push(i);
    while (!q.empty()) {
        int i = q.front(); // top() for priority queue
        ret.push_back(i);
        q.pop();
        for (int x : gr[i])
            if (--indeg[x] == 0) q.push(x);
    }
    return ret;
}

vector<double> multiply(vector<double>& a, vector<double>& b, int cap){
    vector<double> result(min(sz(a)*sz(b),cap+1));
    rep(i,0,sz(a)){
        rep(j,0,sz(b)){
            result[min(i+j,cap)] += a[i]*b[j];
            if (result[min(i+j,cap)] < 0) cout <<"!";
        }
    }
    return result;
}

int choose(int n, int k){
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;
    int result = n;
    for( int i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int n;cin>>n;
    vector<vi> adj(n);
    vector<vi> adjr(n);
    rep(i,0,n-1){
        int a,b;cin>>a>>b;
        adj[b-1].pb(a-1);
        adjr[a-1].pb(b-1);
    }
    vi g,c;
    rep(i,0,n){
        int a,b;cin>>a>>b;
        g.pb(a);
        c.pb(b);
    }

    vi order = topoSort(adj);
    vector<vd> p(n);
    for(int i : order){
        p[i] = {1};
        vd idk = {0.5, 0.5};
        rep(_,0,g[i]) p[i] = multiply(p[i], idk, c[i]);
        for(int j : adjr[i]) p[i] = multiply(p[i], p[j], c[i]);
    }

    double total = 0;
    rep(i,0,sz(p[0])) total += i * p[0][i];
    cout << total << endl;
}
