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

struct UF {
	vi e;
	UF(int n) : e(n, -1) {}
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
	
    int h,w;cin>>h>>w;
    UF uf(w*h);
    bitset<1048576> grid;
    rep(i,0,h){
        string row;cin>>row;
        rep(j,0,w) grid[i*w+j] = row[j] == '1';
    }

    rep(i,0,h)rep(j,0,w){
        if (i && grid[i*w+j] == grid[(i-1)*w+j]) uf.join(i*w+j,(i-1)*w+j);
        if (j && grid[i*w+j] == grid[i*w+j-1]) uf.join(i*w+j, i*w+j-1);
        if (i<h-1 && grid[i*w+j] == grid[(i+1)*w+j]) uf.join(i*w+j, (i+1)*w+j);
        if (j<w-1 && grid[i*w+j] == grid[i*w+j+1]) uf.join(i*w+j, i*w+j+1);
    }

    int n;cin>>n;
    rep(i,0,n){
        int y1,x1,y2,x2;cin>>y1>>x1>>y2>>x2;
        int a1 = (y1-1)*w+(x1-1), a2 = (y2-1)*w+(x2-1);
        // cout << a1 << " " << a2 << " " << uf.find(a1) << " " << uf.find(a2) << endl;
        // cout << grid[a1] << " " << grid[a2] << " ";
        if (uf.find(a1) == uf.find(a2)){
            if (grid[a1]) cout << "decimal\n";
            else cout << "binary\n";
        } else cout << "neither\n";
    }
}
