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

string refff = "A23456789TJQK";

array<int,7> og;
map<array<int,9>,double> cache;
double solve(array<int,9> s){
    // for(int v : s)cout<<v<<' ';cout<<endl;
    auto itr = cache.find(s);
    if(itr!=cache.end())return itr->S;
    if(s[8]==((1<<7)-1)) return 0;
    double ans = 0;
    double rem = 0;
    rep(i,0,8)rem+=s[i];
    rep(i,0,8){
        if(s[i]==0)continue;
        double prob = s[i]/rem;
        int mask = s[8];
        int flip = i;
        while(flip<7 && (s[8]&(1<<flip))==0){
            s[8]|=1<<flip;
            flip=og[flip];
        }
        s[i]--;
        ans += prob * (1 + solve(s));
        s[i]++;
        s[8]=mask;
    }
    return cache[s]=ans;
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    string s;cin>>s;
    array<int,9> init = {4,4,4,4,4,4,4,24,0};
    rep(j,0,7){
        rep(i,0,13)if(refff[i]==s[j]){
            init[min(i,7)]--;
            og[j]=i;
        }
    }
    double exp = solve(init);
    cout<<fixed<<setprecision(10)<<exp<<endl;

    


}


