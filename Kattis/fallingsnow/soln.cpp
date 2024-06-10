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

const int MOD = 1000000009;

vi heightMap;
vi actualSize;

map<tuple<int,int,int>,int> mem;
int ways(int numFound, int lastFoundHeight, int i){
    if (mem.count({numFound,lastFoundHeight,i})) return mem[{numFound,lastFoundHeight,i}];
    if (i == sz(heightMap)) return 0;
    int result;
    if (numFound == 0){
        result = ways(0,lastFoundHeight,i+1) + (actualSize[i]*ways(1,heightMap[i],i+1))%MOD;
    } else if (numFound == 1){
        result = ways(1,lastFoundHeight,i+1);
        if (heightMap[i] > lastFoundHeight){
            result += (actualSize[i]*ways(2,heightMap[i],i+1))%MOD;
        }
    } else if (numFound == 2){
        result = ways(2,lastFoundHeight,i+1);
        if (heightMap[i] > lastFoundHeight){
            result += actualSize[i];
        }
    }
    result %= MOD;
    mem[{numFound,lastFoundHeight,i}] = result;
    return result;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int n;cin>>n;
    vector<pair<ll,ll>> intervals;
    set<ll> coords;
    rep(_,0,n){
        ll a,b;cin>>a>>b;
        intervals.pb({a,b});
        coords.insert(a);
        coords.insert(b);
    }

    map<ll,int> compressed;
    map<int,ll> uncompressed;
    compressed[0] = 0; uncompressed[0] = 0;
    int i1 = 1;
    for(ll coord : coords){
        compressed[coord] = i1;
        uncompressed[i1] = coord;
        if (i1) actualSize.pb(uncompressed[i1] - uncompressed[i1-1]);
        i1++;
    }

    vi starts(i1), ends(i1);
    for(pair<ll,ll> interval : intervals){
        auto [a,b] = interval;
        starts[compressed[a]]++;
        ends[compressed[b]]++;
    }

    heightMap = vi(i1);
    int currHeight = 0;
    rep(i,0,i1){
        currHeight += starts[i];
        heightMap[i] = currHeight;
        currHeight -= ends[i];
    }

    rep(i,0,i1)cout<<heightMap[i]<<" ";cout<<endl;
    rep(i,0,i1)cout<<actualSize[i]<<" ";cout<<endl;
	cout<<ways(0,0,0)<<endl;
}
