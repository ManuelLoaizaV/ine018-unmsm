#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    string s;
    cin >> s;

    vector<int> cnt(26, 0);
    for (int i = 0; i < s.size(); i++) {
        cnt[s[i] - 'a']++;
    }

    bool equilibrio = true;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] % 2 == 1) {
            equilibrio = false;
            break;
        }
    }

    if (equilibrio) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}