#include <iostream>
using namespace std;

void Resolver(void) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    string reloj;
    for (int i = 1; i <= 12; i++) {
        if (a == i || b == i) {
            reloj += 'R';
        } else if (c == i || d == i) {
            reloj += 'A';
        }
    }

    if (reloj == "RARA" || reloj == "ARAR") {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main(void) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        Resolver();
    }
    return 0;
}