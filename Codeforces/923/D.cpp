#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define F first
#define S second
#define pb push_back
typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<int> vi;

struct MinTree {
	typedef pii T;
	static constexpr T unit = pii(INT_MAX,-1);
	T f(T a, T b) { return min(a, b); }
	vector<T> s; int n;
	MinTree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
	void update(int pos, T val) {
		for (s[pos += n] = val; pos /= 2;)
			s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
	}
	T query(int b, int e) { // query [b, e)
		T ra = unit, rb = unit;
		for (b += n, e += n; b < e; b /= 2, e /= 2) {
			if (b % 2) ra = f(ra, s[b++]);
			if (e % 2) rb = f(s[--e], rb);
		}
		return f(ra, rb);
	}
};

struct MaxTree {
	typedef pii T;
	static constexpr T unit = pii(INT_MIN,-1);
	T f(T a, T b) { return max(a, b); }
	vector<T> s; int n;
	MaxTree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
	void update(int pos, T val) {
		for (s[pos += n] = val; pos /= 2;)
			s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
	}
	T query(int b, int e) { // query [b, e)
		T ra = unit, rb = unit;
		for (b += n, e += n; b < e; b /= 2, e /= 2) {
			if (b % 2) ra = f(ra, s[b++]);
			if (e % 2) rb = f(s[--e], rb);
		}
		return f(ra, rb);
	}
};

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int T;cin>>T;
    rep(_,0,T){
        int n;cin>>n;
        MinTree minTree(n,pii(INT_MAX,-1));
        MaxTree maxTree(n,pii(INT_MIN,-1));
        rep(i,0,n){
            int val;cin>>val;
            minTree.update(i,pii(val,i));
            maxTree.update(i,pii(val,i));
        }
        int q;cin>>q;
        rep(x,0,q){
            int l,r;cin>>l>>r;
            pii p1,p2;
            p1 = minTree.query(l-1,r);
            p2 = maxTree.query(l-1,r);
            //cout<<p1.F<<" "<<p1.S<<" "<<p2.F<<" "<<p2.S<<"\n";
            if (p1.F == p2.F){
                cout<<-1<<" "<<-1<<"\n";
            } else {
                cout<<p1.S+1<<" "<<p2.S+1<<"\n";
            }
        }
        cout<<"\n";
    }
}