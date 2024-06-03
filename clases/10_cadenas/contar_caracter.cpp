#include <iostream>
using namespace std;

int ContarCaracter(char c, string s) {
    int n = s.size();
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == c) {
            cnt++;
        }
    }
    return cnt;
}

int main(void) {
    cout << ContarCaracter('z', "Manuel") << endl;
    cout << ContarCaracter('m', "Mi mama me mima con mimi") << endl;
    cout << ContarCaracter(' ', "   ") << endl;
    cout << ContarCaracter('a', "") << endl;
    return 0;
}