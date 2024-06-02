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
typedef array<int,4> rect;

bool overlap(rect r1, rect r2){
    return r1[2]+r1[0] > r2[2] && r1[2] < r2[2]+r2[0] && r1[3] < r2[3]+r2[1] && r1[3]+r1[1] > r2[3];
}

int area(rect r){ return r[0] * r[1]; }

map<int,int> mem;
vi nos;
vector<rect> rects;
int maxArea(int& n, int mask){
    if (mem.count(mask)) return mem[mask];
    if (mask == (1<<n)-1) return 0;
    int best = 0;
    rep(i,0,n){
        if ((mask & (1<<i)) == 0){
            best = max(best, maxArea(n, mask | (1<<i) | nos[i]) + area(rects[i]));
        }
    }
    mem[mask] = best;
    return best;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    while (1){
        int n;cin>>n;
        if (n == 0) break;
        mem = map<int,int>();
        nos = vi(n);
        rects = vector<rect>(n);
        rep(i,0,n){
            int w,h,x,y;cin>>w>>h>>x>>y;
            rects[i] = {w,h,x,y};
            rep(j,0,i){
                if (overlap(rects[i],rects[j])){
                    nos[i] |= (1<<j);
                    nos[j] |= (1<<i);
                }
            }
        }
        cout << maxArea(n,0) << endl;
    }
}
