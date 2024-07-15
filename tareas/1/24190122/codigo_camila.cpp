#include <iostream>
#include <cmath>
//unu
using namespace std;

// Función que verifica si los segmentos se intersectan basándose en las condiciones proporcionadas
bool doIntersect(int a, int b, int c, int d) {
    // Caso NO
    if (abs(a - b) == 1 || (a == 12 && b == 1) || (a == 1 && b == 12)) {
        return false;
    }
    if (abs(c - d) == 1 || (d == 12 && c == 1) || (c == 1 && d == 12)) {
        return false;
    }
    // Caso SI
    if (a == 12 && b != 12) {
        return (c < b && b < d) || (d < b && b < c);
    }
    if (b > a) {
        return (c < a && a < d && d < b) || (d < a && a < c && c < b)||(a < d && d < b && b<c)||(a < c && c < b && b < d);
    }
    if (b < a) {
        return (b < c && c < a && a < d) || (b < d && d < a && a < c);
    }

    if (b == 12 && a != 12) {
    return (c < a && a < d) || (d < a && a < c);
    }
    if (a > b) {
    return (c < b && b < d && d < a) || (d < b && b < c && c < a) || (b < d && d < a && a < c) || (c < d && d < b && b < a);
    }
    if (a < b) {
    return (a < c && c < b && b < d) || (a < d && d < b && b < c);
    }

    return false;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        if (doIntersect(a, b, c, d)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
