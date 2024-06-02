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
typedef bitset<32> bs;

string s;
int n,k;
bs dp[41][401][42];
bs zero = bs(0);

bs possible(int ns, int nas, int i){
    // cout << nw;
    if (dp[ns][nas][i] != zero) return dp[ns][nas][i];
    if (i == n) return bs(1);
    bs nw(0);
    if (s[i] == '?') nw |= possible(ns,nas,i+1);
    if (s[i] == 'N' || s[i] == '?') nw |= possible(ns+1,nas,i+1);
    if (s[i] == 'A' || s[i] == '?') nw |= possible(ns,nas+ns,i+1);
    if (s[i] == 'C' || s[i] == '?') nw |= (possible(ns,nas,i+1) << nas);
    cout << ns << " " << nas << " " << i << " " << nw << endl;
    return dp[ns][nas][i] = nw;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    
    rep(i,0,41)rep(j,0,401)rep(k,0,42)dp[i][j][k] = bs(0);

    cin>>n>>k>>s;
    bs poss = possible(0,0,0);
    // cout << poss << endl;
    // cout << "=============================================\n";
    if (poss[k]){
        // traceback
        int ns = 0, nas = 0, i = 0;
        vector<char> out;
        while (i < n){
            cout << i << endl;
            cout << i << " " << k << " " << ns << " " << nas << " " << dp[ns+1][nas][i] << " " << dp[ns][nas+ns][i] << " " << dp[ns][nas][i] << " ";//<< endl;
            // if (nacs == k && s[i] == '?') {
            //     // cout << "/" << endl;
            //     out.pb('Z');
            // } else if (nacs == k) {
            //     // cout << "." << endl;
            //     out.pb(s[i]);
            // } else if (s[i] == 'N' || dp[ns+1][nas][i][k-nacs]){
            if (s[i] != '?'){
                cout << "!" << " ";
                if (s[i] == 'N') ns++;
                else if (s[i] == 'A') nas += ns;
                else if (s[i] == 'C') k -= nas;
                out.pb(s[i]);
            } else if (dp[ns][nas][i][k]){
                cout << "Z" << " ";
                out.pb('Z');
            } else if (dp[ns+1][nas][i][k]){
                cout << "N" << " ";
                out.pb('N');
                ns++;
            } else if (dp[ns][nas+ns][i][k]){
                cout << "A" << " ";
                out.pb('A');
                nas += ns;
            } else if (k-nas >= 0 && dp[ns][nas][i][k]){
                cout << "C" << " ";
                out.pb('C');
                k -= nas;
            } else {
                cout << "uh oh..." << endl;
            }
            cout << endl;
            // cout << out.back() << endl;
            i++;
        }
        cout << string(all(out)) << endl;
    } else {
        cout << -1 << endl;
    }
}
