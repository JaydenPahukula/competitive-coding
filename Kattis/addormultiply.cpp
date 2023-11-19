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


ll euclid(ll a, ll b, ll &x, ll &y) {
    if (!b) return x = 1, y = 0, a;
    ll d = euclid(b, a % b, y, x);
    return y -= a/b * x, d;
}

const ll mod = 1e9+7;
struct Mod {
    ll x;
    Mod() : x(0) {}
    Mod(ll xx) : x(xx % mod) {}
    Mod operator+(Mod b) { return Mod((x + b.x) % mod); }
    Mod operator-(Mod b) { return Mod((x - b.x + mod) % mod); }
    Mod operator*(Mod b) { return Mod((x * b.x) % mod); }
    Mod operator/(Mod b) { return *this * invert(b); }
    Mod invert(Mod a) {
        ll x, y, g = euclid(a.x, mod, x, y);
        assert (g == 1); return Mod((x + mod) % mod);
    }
    Mod operator^(ll e) {
        if (!e) return Mod(1);
        Mod r = *this ^ (e / 2); r = r * r;
        return e&1 ? *this * r : r;
    }
};

typedef Mod T;
T unit = 1;
struct Tree {
    T f(T a, T b) { return a*b; }
    vector<T> s; int n;
    Tree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
    void update(int pos, T val){
        for (s[pos += n] = val; pos /= 2;)
            s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
    }
    T query (int b, int e) {
        T ra = unit, rb = unit;
        for (b += n, e += n; b < e; b /= 2, e /= 2) {
            if (b % 2) ra = f(ra, s[b++]);
            if (e % 2) rb = f(s[--e], rb);
        }
        return f(ra, rb);
    }
};

struct Soln {
    Mod tot;
    set<pii> ranges;
    Tree sg;
    string expr;
    Soln(string expr) : expr(expr), sg(1+sz(expr)/2), tot(0) {
        int prev = 0;
        for(int i = 0; i < sz(expr); i+=2) sg.update(i/2,expr[i]-'0');
        for(int i = 1; i<sz(expr);i+=2){
            if(expr[i]=='*'){
                continue;
            }else{
                ranges.insert({prev,i/2});
                prev=1+i/2;
            }
        }
        ranges.insert({prev,sz(expr)/2});
        for(auto p : ranges) tot = tot + sg.query(p.F, p.S+1);
    }
    void toggle(int pos){
        if(expr[pos*2-1]=='+'){
            auto aft = ranges.lower_bound({pos,pos});
            auto bef = prev(aft);
            tot = tot - sg.query(aft->F, aft->S+1);
            tot = tot - sg.query(bef->F, bef->S+1);
            ranges.insert({bef->F, aft->S});
            tot = tot + sg.query(bef->F, aft->S+1);
            ranges.erase(aft);
            ranges.erase(bef);
        }else{
            auto r = prev(ranges.lower_bound({pos,pos}));
            tot = tot - sg.query(r->F, r->S+1);
            pii left = {r->F,pos-1};
            pii right = {pos,r->S};
            ranges.insert(left);
            ranges.insert(right);
            tot = tot + sg.query(left.F, left.S+1);
            tot = tot + sg.query(right.F, right.S+1);
            ranges.erase(r);

        }
        expr[pos*2-1]=(expr[pos*2-1]=='+'?'*':'+');
    }
    void upd(int pos, int v){
        auto r = *prev(ranges.lower_bound({pos+1,-1}));
        tot = tot - sg.query(r.F, r.S+1);
        sg.update(pos,v);
        tot = tot + sg.query(r.F, r.S+1);
    }
    void swapp(int p1, int p2){
        swap(expr[p1*2-2],expr[p2*2-2]);
        upd(p1-1,expr[p1*2-2]-'0');
        upd(p2-1,expr[p2*2-2]-'0');
    }
};

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int n,m;cin>>n>>m;
    string s;cin>>s;
    Soln* main = new Soln(s);
    cout<<main->tot.x<<'\n';
    for(int i = 1; i < sz(s); i+=2) s[i]=(s[i]=='+'?'*':'+');
    Soln* alt = new Soln(s);
    rep(_,0,m){
        char op; cin>>op;
        if(op=='s'){
            int a,b;cin>>a>>b;
            main->swapp(a,b);
            alt->swapp(a,b);
        }else if(op=='f'){
            int i;cin>>i;
            main->toggle(i);
            alt->toggle(i);
        }else{
            assert(op=='a');
            swap(main,alt);
        }
        cout<<main->tot.x<<'\n';
    }

}


