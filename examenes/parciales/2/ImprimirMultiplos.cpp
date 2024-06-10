#include <iostream>
using namespace std;

void ImprimirMultiplos(int n, int m) {
    cout << "Los " << m << " primeros múltiplos de " << n << " son";
    for (int i = 1; i <= m; i++) {
        if (i == m) {
            cout << " y";
        } else if (i > 1) {
            cout << ",";
        }
        cout << " " << i * n;
    }
    cout << "." << endl;
}

int main(void) {
    ImprimirMultiplos(3, 5);
    ImprimirMultiplos(7, 3);
    return 0;
}