// Dado un número natural n, imprimir la suma de los primeros n cuadrados y el valor de esta.

// Input: n >= 1 natural.
// Output: 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6

// Ejemplos
// Input: 1
// Output: 1^2 = 1

// Input: 3
// Output: 1^2 + 2^2 + 3^2 = 14

// Input: 5
// Output: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55

// 1. Solicitar al usuario que ingrese el valor de n.
// 2. Leer el valor de n.
// 3. (Opcional pues usar la fórmula) Crear variable para acumular la suma de cuadrados.
// 4. Utilizar un bucle for para imprimir la sumatoria. (1^2 + 2^2 + 3^2 + 4^2 + 5^2)
// 5. Imprimir la suma de cuadrados. (= 55)

#include <iostream>
using namespace std;

int main(void) {
    cout << "Ingrese un numero entero: ";
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i > 1) {
            cout << " + ";
        }
        cout << i << "^2";
    }
    int suma = n * (n + 1) * (2 * n + 1) / 6;
    cout << " = " << suma << endl;
    return 0;
}
