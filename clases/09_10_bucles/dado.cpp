#include <iostream>
#include <cstdlib>
using namespace std;

int main(void) {
    int suerte = 3;

    // Asume que suerte está definida
    // como un entero en [1, 6].

    int lanzamiento = -1;
    int maximo_lanzamiento = -1;
    int numero_lanzamientos = 0;

    while (lanzamiento != suerte) {
        // Lanzamos un dado y obtenemos un número en [1, 6].
        lanzamiento = 1 + rand() % 6;
        numero_lanzamientos++;

        cout << "Lanzamiento " << numero_lanzamientos << ": " << lanzamiento << endl;

        // En caso el número obtenido sea el mayor
        // hasta ahora, lo guardamos.
        if (lanzamiento > maximo_lanzamiento) {
            maximo_lanzamiento = lanzamiento;
        }
    }

    cout << "Numero de la suerte: " << lanzamiento << endl;
    cout << "Maximo valor obtenido: " << maximo_lanzamiento << endl;
    cout << "Numero de lanzamientos: " << numero_lanzamientos << endl;
    return 0;
}