#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int n, l;
    cin >> n >> l;

    vector<string> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (s[j] < s[i]) {
                swap(s[i], s[j]);
            }
        }
    }

    string resultado;
    for (int i = 0; i < n; i++) {
        resultado += s[i];
    }

    cout << resultado << endl;
    return 0;
}