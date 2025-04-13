#include <iostream>
using namespace std;

bool ComienzaCon(string s, string t) {
    if (t.size() > s.size()) {
        return false;
    }
    return s.substr(0, t.size()) == t;
}

int main(void) {
    cout << ComienzaCon("abc", "a") << endl;
    cout << ComienzaCon("abc", "ab") << endl;
    cout << ComienzaCon("abc", "abc") << endl;
    cout << ComienzaCon("abc", "abcd") << endl;
    cout << ComienzaCon("abc", "b") << endl;
    cout << ComienzaCon("abc", "c") << endl;
    return 0;
}