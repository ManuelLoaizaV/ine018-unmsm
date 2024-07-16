#include <iostream>
#include <iomanip>
using namespace std;

void Wallis(long double limite, char sucesion) {
    // Si el límite es mayor a 0.5 o la sucesión no es 'a' ni 'b', no se hace nada.
    if (limite > 0.5L || sucesion != 'a' && sucesion != 'b') {
        return;
    }

    // Inicializamos el producto parcial y nuestro índice.
    long double producto = 1.0L;
    int k = 0;

    // Iteramos y multiplicamos cada término
    // hasta que el producto sea menor o igual al límite.
    while (producto > limite) {
        k++;
        int numerador, denominador;
        // Determinamos la fracción según la sucesión especificada.
        if (sucesion == 'a') {
            numerador = 2 * k - 1;
            denominador = 2 * k;
        } else {
            numerador = 2 * k;
            denominador = 2 * k + 1;
        }

        // Imprimimos el término actual en el formato adecuado.
        if (k > 1) {
            cout << " * ";
        }
        cout << numerador << '/' << denominador;

        // Acumulamos el término actual en el producto parcial.
        producto *= (long double)numerador / denominador;
    }

    // Imprimimos el producto parcial con tres dígitos de precisión.
    cout << " = " << fixed << setprecision(3) << producto << endl;
}

int main(void) {
    Wallis(1.0L, 'a');
    Wallis(1.0L, 'b');
    Wallis(1.0L, 'c');
    Wallis(0.5L, 'a');
    Wallis(0.5L, 'b');
    Wallis(0.5L, 'c');
    Wallis(0.375L, 'a');
    Wallis(0.375L, 'b');
    Wallis(0.375L, 'c');
    Wallis(0.35L, 'a');
    Wallis(0.35L, 'b');
    Wallis(0.35L, 'c');
    return 0;
}