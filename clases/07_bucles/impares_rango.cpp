// Input: l r
// Output: Imprimir en pantalla los números impares en ese rango.
// En caso no haya números, imprimir ":("

// Ejemplo 1
// Input: 2 10
// Output: 3 5 7 9

// Ejemplo 2
// Input: 1 3
// Output: 1 3

// Ejemplo 3:
// Input: 7 -2
// Output: -1 1 3 5 7

// Ejemplo 4
// Input: 8 8
// Output: :(

#include <iostream>
using namespace std;

int main(void) {
    cout << "Ingrese el rango [l, r]: ";
    int l, r;
    cin >> l >> r;

    if (l > r) {
        int k = l;
        l = r;
        r = k;
    }

    bool found = false;
    for (int i = l; i <= r; i = i + 1) {
        if (i % 2 != 0) {
            if (found) {
                cout << " ";
            }
            cout << i;
            found = true;
        }
    }

    if (!found) {
        cout << ":(";
    }
    cout << endl;
    return 0;
}