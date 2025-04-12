#include <iostream>
using namespace std;

int main(void) {
    // Desde i igual a 1 hasta 5.
    // Como no actualizaremos el valor de i en otro lugar,
    // la intención de este bucle es realizar el bloque 5 veces.
    for (int i = 1; i <= 5; i++) {
        // Desde j igual a 1 hasta i.
        // Como no utilizaremos la variable j dentro del bloque,
        // podemos interpretar el siguiente bucle como
        // imprimir i veces el valor de i.
        for (int j = 1; j <= i; j++) {
            cout << i;
        }
        // Luego de imprimir una fila completa,
        // imprimiremos un salto de línea.
        cout << endl;
    }

    // Salida:
    // 1
    // 22
    // 333
    // 4444
    // 55555

    return 0;
}