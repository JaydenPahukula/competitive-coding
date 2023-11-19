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

template <class T> int sgn(T x) { return (x > 0) - (x < 0);}
template<class T>
struct Point {
    typedef Point P;
    T x, y;
    explicit Point(T x=0, T y=0) : x(x), y(y) {}
    bool operator<(P  p) const { return tie(x, y) < tie(p.x, p.y); }
    bool operator==(P p) const { return tie(x, y) == tie(p.x, p.y); }
    P operator+(P p) const { return P(x+p.x, y+p.y); }
    P operator-(P p) const { return P(x-p.x, y-p.y); }
    P operator*(T d) const { return P(x*d, y*d); }
    P operator/(T d) const { return P(x/d, y/d); }
    T dot(P p) const { return x*p.x + y*p.y; }
    T cross(P p) const { return x*p.y - y*p.x; }
    double angle() const {return atan2(y, x); }
    T dist() const {return x*x + y*y; }
};

const double PI = 3.141592653589793;

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    

    int n; cin >> n;
    vector<Point<ll>> p(n); 
    rep(i, 0, n) {
        ll x, y; cin >> x >> y;
        p[i] = Point<ll>(x, y);
    }

    ll xc, yc, x0, y0; cin >> x0 >> y0 >> xc >> yc;
    Point<ll> v = Point(xc, yc) - Point(x0, y0);

    vector<Point<ll>> e(n);
    rep(i, 0, n-1) {
        e[i] = p[i+1]-p[i];
    }
    e[n-1] = p[0] - p[n-1];


    double t=0;
    rep(i, 0, n-1) {
        double a=e[i+1].angle()-e[i].angle();
        if (a > PI) a-= 2 * PI;
        if (a < -PI) a += 2 * PI;
        t+=a;
    }

    double a=e[0].angle()-e[n-1].angle();
    if (a > PI) a-= 2 * PI;
    if (a < -PI) a += 2 * PI;
    t+=a;

    rep (i, 1, n) {
        Point<ll> r = Point(x0, y0) - p[i];

        if (r==Point<ll>(0,0)) {
            if (e[i].cross(v) == 0 || e[i-1].cross(v)==0) {
                cout << "?\n";
            } else if ((e[i].cross(v) > 0) == (t > 0)) {
                if ((e[i-1].cross(v) > 0) == (t > 0)) {
                    cout << "inside\n";
                } else {
                    cout << "?\n";
                }
            } else {
                if ((e[i-1].cross(v) > 0) == (t > 0)) {
                    cout << "?\n";
                } else {
                    cout << "outside\n";
                }
            }
            return 0;
        }
        else if (e[i].cross(r) == 0 && e[i].dot(r) > 0 && r.dist() < e[i].dist()) {
            if (e[i].cross(v) == 0) {
                cout << "?\n";
            } else if ((e[i].cross(v) > 0) == (t > 0)) {
                cout << "inside\n";
            } else {
                cout << "outside\n";
            }
            return 0;
        }
    }

    Point<ll> r = Point(x0, y0) - p[0];
    if (r==Point<ll>(0,0)) {
        if (e[0].cross(v) == 0 || e[n-1].cross(v)==0) {
            cout << "?\n";
        } else if ((e[0].cross(v) > 0) == (t > 0)) {
            if ((e[n-1].cross(v) > 0) == (t > 0)) {
                cout << "inside\n";
            } else {
                cout << "?\n";
            }
        } else {
            if ((e[n-1].cross(v) > 0) == (t > 0)) {
                cout << "?\n";
            } else {
                cout << "outside\n";
            }
        }
    }
    else {
        if (e[0].cross(v) == 0) {
            cout << "?\n";
        } else if ((e[0].cross(v) > 0) == (t > 0)) {
            cout << "inside\n";
        } else {
            cout << "outside\n";
        }
    }

    return 0;
}


