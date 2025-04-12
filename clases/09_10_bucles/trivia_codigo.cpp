#include <iostream>
using namespace std;

// Queremos un código que produzca la siguiente salida:
// 1
// 12
// 123
// 1234
// 12345

int main(void) {
    // Queremos que el resultado tenga 5 filas, por lo que
    // definiremos un bucle que itere 5 veces su contenido.
    for (int i = 0; i < 5; i++) {
        // Notamos que la primera fila tiene un elemento,
        // la segunda tiene dos, y así sucesivamente.
        
        // Por ejemplo, nuestra tercera fila está representada por i = 2.
        // Como esta fila tiene que imprimir 3 números,
        // el siguiente bucle iteraría los valores de j = 0, 1, 2.
        // Ahora, queremos imprimir 123, por lo que imprimir j + 1 sería lo ideal.
        for (int j = 0; j <= i; j++) {
            cout << j + 1;
        }

        // Luego de cada fila imprimiremos un salto de línea.
        cout << endl;
    }
    return 0;
}