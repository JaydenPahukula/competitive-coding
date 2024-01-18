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

int findLeft(int x, vi& left){
    if (left[x] == x) return x;
    if (left[x] == -1) return -1;
    left[x] = findLeft(left[x], left);
    return left[x];
}
int findRight(int x, vi& right){
    if (right[x] == x) return x;
    if (right[x] == -1) return -1;
    right[x] = findRight(right[x], right);
    return right[x];
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int t;cin>>t;
    rep(_,0,t){
        int n;cin>>n;
        vi attack = vi(n,0);
        rep(i,0,n)cin>>attack[i];
        vi defense = vi(n,0);
        rep(i,0,n)cin>>defense[i];

        vi left = vi(n,0);
        vi right = vi(n,0);
        rep(i,0,n){
            left[i]=i;
            right[i]=i;
        }
        vector<bool> alive = vector<bool>(n,true);

        vi out;
        rep(i,0,n){
            vi damage = vi(n,0);
            rep(j,0,n){
                if (!alive[j]) continue;
                if (j > 0){
                    int target = findLeft(j-1, left);
                    if (target != -1) damage[target] += attack[j];
                }
                if (j < n-1){
                    int target = findRight(j+1, right);
                    if (target != -1) damage[target] += attack[j];
                }
            }
            int killCount = 0;
            rep(j,0,n){
                if (alive[j] && damage[j] > defense[j]){
                    alive[j] = false;
                    if (j == 0) left[j] = -1;
                    else left[j] = left[j-1];
                    if (j == n-1) right[j] = -1;
                    else right[j] = right[j+1];
                    killCount++;
                }
            }
            out.push_back(killCount);
        }
        rep(i,0,out.size()){
            cout<<out[i]<<" ";
        }
        cout<<endl;
    }
}