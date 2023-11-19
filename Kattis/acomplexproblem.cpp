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


vi val, comp, z, cont;
int Time, ncomps;
template<class G, class F> int dfs(int j, G& g, F& f) {
    int low = val[j] = ++Time, x; z.push_back(j);
    for (auto e : g[j]) if (comp[e] < 0)
        low = min(low, val[e] ?: dfs(e,g,f));
    
    if (low == val[j]) {
        do {
            x = z.back(); z.pop_back();
            comp[x] = ncomps;
            cont.push_back(x);
        } while (x != j);
        f(cont); cont.clear();
        ncomps++;
    }
    return val[j] = low;
}
template<class G, class F> void scc(G& g, F f) {
    int n = sz(g);
    val.assign(n, 0); comp.assign(n, -1);
    Time = ncomps = 0;
    rep(i,0,n) if (comp[i] < 0) dfs(i, g, f);
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int n,m;cin>>n>>m;
    set<string> sets;
    vector<pair<string,string>> e1(n),e2(m);
    rep(i,0,n){
        string a,b;cin>>a>>b;
        sets.insert(a);
        sets.insert(b);
        e1[i]={a,b};
    }
    rep(i,0,m){
        string a,b;cin>>a>>b;
        sets.insert(a);
        sets.insert(b);
        e2[i]={a,b};
    }
    vector<string> names(all(sets));
    int z = sz(names);
    map<string,int> rev;rep(i,0,z){
        rev[names[i]]=i;
        // cout<<names[i]<<": "<<i<<endl;
    }

    vector<vi> adj1(z);
    for(auto p : e1)adj1[rev[p.F]].pb(rev[p.S]);
    vector<vi> adj2(z);
    for(auto p : e2)adj2[rev[p.F]].pb(rev[p.S]);

    vi p(z,-1);
    function<int(int)> find = [&](int x){
        if(p[x]<0) return x;
        return p[x]=find(p[x]);
    };
    int mx = 0;
    scc(adj1,[&](vi comp){
        mx++;
        rep(i,1,sz(comp)) {
            int a = find(comp[0]);
            int b = find(comp[i]);
            if(a==b) continue;
            p[a]=b;
        }
    });
    vector<vi> rev2(z);
    rep(i,0,z)rev2[find(i)].pb(i);
    vi dp(z,-1);
    function<int(int)> dfs = [&](int loc){
        loc=find(loc);
        if(dp[loc]!=-1) return dp[loc];
        int far = 0;
        for(int src : rev2[loc]){
            for(int con : adj1[src])if(find(con)!=loc)far=max(far,dfs(con));
            for(int con : adj2[src]) far=max(far,1+dfs(con));
        }
        return dp[loc]=far;
    };
    int smol = 0;
    rep(i,0,z)smol=max(smol,dfs(i));
    // for(int v : dp)cout<<v<<' ';cout<<endl;


    cout<<smol+1<<' '<<mx<<endl;

}


