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

vector<vi> chain;
unordered_set<int> highest;
unordered_map<int, int> mem;

int find(int x){
    //cout << "called find " << x << endl;
    if (highest.count(x) > 0) return 0;
    if (mem.count(x) == 0){
        int mn = pow(10,9)+1;
        for (int parent : chain[x]){
            //cout << "parent: " << parent << endl;
            int r = find(parent);
            if (r < mn) mn = r;
        }
        mem[x] = mn+1;
    }
    return mem[x];
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int n; cin >> n;
    vi h(n, -1);
    int m = 0;
    rep(i, 0, n){
        cin >> h[i];
        if (h[i] > m) m = h[i];
    }

    highest = unordered_set<int>();
    rep(i, 0, n){
        if (h[i] == m) highest.insert(i);
    }

    chain = vector<vi>(n, vi());
    
    // iterate right
    vi a;
    rep(i, 0, n){
        while (a.size() > 0 && h[i] >= h[a[a.size()-1]]) a.pop_back();
        if (a.size() > 0) chain[i].push_back(a[a.size()-1]);
        a.push_back(i);
    }
    // iterate left
    a.clear();
    for(int i = n-1; i > -1; i--){
        while (a.size() > 0 && h[i] >= h[a[a.size()-1]]) a.pop_back();
        if (a.size() > 0) chain[i].push_back(a[a.size()-1]);
        a.push_back(i);
    }

    rep(i, 0, n){
        cout << find(i) << " ";
    }
    cout << endl;
}