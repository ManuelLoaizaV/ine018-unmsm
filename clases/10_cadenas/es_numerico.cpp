#include <iostream>
using namespace std;

bool EsNumerico(string s) {
    for (int i = 0; i < s.size(); i++) {
        if (!('0' <= s[i] && s[i] <= '9')) {
            return false;
        }
    }
    return true;
}

int main(void) {
    cout << EsNumerico("3.1415") << endl;
    cout << EsNumerico("31415") << endl;
    cout << EsNumerico("xyz123") << endl;
    cout << EsNumerico("123") << endl;
    cout << EsNumerico("diez") << endl;
    cout << EsNumerico("10") << endl;
    return 0;
}