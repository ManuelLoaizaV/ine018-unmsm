#include <iostream>
using namespace std;

int ContarDigitosPares(int numero) {
    // Caso borde: cero tiene 1 dígito par.
    if (numero == 0) {
        return 1;
    }
    int pares = 0;
    // Mientras el número tiene dígitos.
    while (numero > 0) {
        // Obtenemos el último dígito.
        int digito = numero % 10;
        // Eliminamos el último dígito.
        numero /= 10;
        // Contamos si el dígito es par.
        if (digito % 2 == 0) {
            pares++;
        }
    }
    return pares;
}

int main(void) {
    cout << ContarDigitosPares(8546587) << endl;
    return 0;
}