#include <iostream>
using namespace std;

string Revertir(string s) {
    int n = s.size();
    for (int i = 0; i < n / 2; i++) {
        swap(s[i], s[n - 1 - i]);
    }
    return s;
}

bool EsPalindromo(string s) {
    return s == Revertir(s);
}

// bool EsPalindromo(string s) {
//     int n = s.size();
//     for (int i = 0; i < n / 2; i++) {
//         if (s[i] != s[n - 1 - i]) {
//             return false;
//         }
//     }
//     return true;
// }

int main(void) {
    cout << EsPalindromo("anitalavalatina") << endl;
    cout << EsPalindromo("abacaba") << endl;
    cout << EsPalindromo("xyz") << endl;
    return 0;
} 