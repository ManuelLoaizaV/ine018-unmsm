#include <iostream>
using namespace std;

string Revertir(string s) {
    int n = s.size();
    for (int i = 0; i < n / 2; i++) {
        swap(s[i], s[n - 1 - i]);
    }
    return s;
}

int main(void) {
    cout << Revertir("abel") << endl;
    cout << Revertir("jake") << endl;
    cout << Revertir("anitalavalatina") << endl;
    return 0;
} 