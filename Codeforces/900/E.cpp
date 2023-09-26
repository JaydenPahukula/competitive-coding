#include <bits/stdc++.h>
using namespace std;

struct Tree {
	typedef int T;
	static constexpr T unit = INT_MIN;
	T f(T a, T b) { 
        cout << "comparing " << a << " & " << b << endl;
        return (a & b); } // (any associative fn)
	vector<T> s; int n;
	Tree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
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
    for (int asdf = 0; asdf < T; asdf++){

        int n;cin>>n;
        Tree segTree(n);
        for (int i = 0; i < n; i++){
            int x;cin>>x;
            segTree.update(i+1, x);
        }
        cout << "-------" << endl;
        cout << segTree.query(1, 1) << endl;
        cout << segTree.query(1, 2) << endl;
        cout << segTree.query(1, 3) << endl;

        cout << (15 & 14);

        // int q;cin>>q;
        // for (int i = 0; i < q; i++){
        //     int l,k;cin>>l>>k;

        //     int lo=l,hi=n,m,result;
        //     while (lo < hi){
        //         //cout << lo << " " << hi << " " << m << endl;
        //         m = (lo+hi)/2;
        //         result = segTree.query(l,m);
        //         if (result < k) hi=m;
        //         else lo=m+1;
        //     }

        //     if (lo == l) cout << "=====" << -1 << " ";
        //     else cout << "=====" << lo << " ";
        // }
        // cout << "\n";
    }
}