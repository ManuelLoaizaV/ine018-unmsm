#include <iostream>
#include <iomanip>
using namespace std;

void Armonica(long double limite) {
    // Si el límite es menor a 1, no se imprime nada.
    if (limite < 1.0L) {
        return;
    }

    // Inicializamos la suma parcial y nuestro índice.
    long double suma = 0.0L;
    int k = 0;

    // Iteramos y sumamos cada término hasta que
    // la suma alcance o exceda el límite.
    while (suma < limite) {
        k++;

        // Imprimimos el término actual en el formato adecuado.
        if (k == 1) {
            cout << '1';
        } else {
            cout << " + 1/" << k;
        }

        // Acumulamos el término actual en la suma parcial.
        suma += 1.0L / k;
    }

    // Imprimimos la suma parcial con tres dígitos de precisión.
    cout << " = " << fixed << setprecision(3) << suma << endl;
}

int main(void) {
    Armonica(2.0L);
    Armonica(0.0L);
    Armonica(1.0L);
    Armonica(1.5L);
    Armonica(2.7L);
    return 0;
}
