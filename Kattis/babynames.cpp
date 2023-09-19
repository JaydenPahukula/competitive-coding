#include <string>
#include <iostream>
using namespace std;
#include <bits/extc++.h> /** keep-include */
using namespace __gnu_pbds;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
    tree<string, null_type, less<string>, rb_tree_tag, tree_order_statistics_node_update> m,f;
    while(true){
        int type;cin >> type;
        if (type == 0) break;
        if (type == 1){
            string name;cin >> name;
            int gender;cin >> gender;
            if (gender != 2) m.insert(name);
            if (gender != 1) f.insert(name);
        }
        if (type == 2){
            string name;cin >> name;
            auto findm = m.find(name);
            if(findm != m.end()) m.erase(findm);
            auto findf = f.find(name);
            if(findf != f.end()) f.erase(findf);
        }
        if (type == 3){
            string start,end;cin >> start >> end;
            int gender;cin >> gender;
            int out = 0;
            if (gender != 2) out += m.order_of_key(end)-m.order_of_key(start);
            if (gender != 1) out += f.order_of_key(end)-f.order_of_key(start);
            cout << out << "\n";
        }
    }
}