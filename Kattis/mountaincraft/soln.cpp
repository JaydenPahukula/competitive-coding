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

    const int SIZE = 640;

    int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int q,w;cin>>q>>w;
    vector<pii> qs;
    set<int> cords;
    rep(i,0,q){
        int x,y;cin>>x>>y;
        int a = x-y, b = x+y;
        qs.pb({a,b});
        cords.insert(a);
        cords.insert(b);
    }

    // compress
    map<int,int> compressed, uncompressed;
    int i = 0;
    for(int cord : cords){
        compressed[cord] = i;
        uncompressed[i] = min(max(cord,0),w);
        i++;
    }
    uncompressed[i] = w;

    vector<vi> chunks(SIZE, vi(SIZE));
    vi chunkCounts(SIZE), counts(SIZE,0), chunkSize(SIZE);
    rep(i,0,SIZE) chunkSize[i] = uncompressed[SIZE*(i+1)] - uncompressed[SIZE*i];
    set<pii> known;
    cout << fixed << setprecision(7);
    for (pii query : qs){

        int add = 1;
        if (known.count(query)){
        known.erase(query);
        add = -1;
        } else known.insert(query);

        int left = compressed[query.F];
        int right = compressed[query.S];
        int lChunk = left/SIZE;
        int rChunk = right/SIZE;

        if (lChunk == rChunk){
        rep(i,left-(SIZE*lChunk),right-(SIZE*lChunk)){
            int old = chunks[lChunk][i];
            chunks[lChunk][i] += add;
            if (old != 0 && chunks[lChunk][i] == 0){
            counts[lChunk] -= uncompressed[SIZE*lChunk+i+1] - uncompressed[SIZE*lChunk+i];
            } else if (old == 0 && chunks[lChunk][i] != 0){
            counts[lChunk] += uncompressed[SIZE*lChunk+i+1] - uncompressed[SIZE*lChunk+i];
            }
        }
        } else {
        rep(i,left-(SIZE*lChunk),SIZE){
            int old = chunks[lChunk][i];
            chunks[lChunk][i] += add;
            if (old != 0 && chunks[lChunk][i] == 0){
            counts[lChunk] -= uncompressed[SIZE*lChunk+i+1] - uncompressed[SIZE*lChunk+i];
            } else if (old == 0 && chunks[lChunk][i] != 0){
            counts[lChunk] += uncompressed[SIZE*lChunk+i+1] - uncompressed[SIZE*lChunk+i];
            }
        }
        rep(i,lChunk+1,rChunk){
            chunkCounts[i] += add;
        }
        rep(i,0,right-(SIZE*rChunk)){
            int old = chunks[rChunk][i];
            chunks[rChunk][i] += add;
            if (old != 0 && chunks[rChunk][i] == 0){
            counts[rChunk] -= uncompressed[SIZE*rChunk+i+1] - uncompressed[SIZE*rChunk+i];
            } else if (old == 0 && chunks[rChunk][i] != 0){
            counts[rChunk] += uncompressed[SIZE*rChunk+i+1] - uncompressed[SIZE*rChunk+i];
            }
        }
        }

        int count = 0;
        rep(i,0,SIZE){
        if (chunkCounts[i]) count += chunkSize[i];
        else count += counts[i];
        }
        cout << count * sqrt(2) << "\n";
    }
}
