#include <iostream>
using namespace std;

string Revertir(string s) {
    string r;
    int n = s.size();
    for (int i = n - 1; i >= 0; i--) {
        r += s[i];
    }
    return r;
}

string EnteroACadena(int n) {
    // Un caso borde a nuestra lógica es cuando el número
    // está conformado únicamente por el caracter cero.
    if (n == 0) {
        return "0";
    }

    // Cuando el número es negativo,
    // reconstruiremos su valor absoluto
    // y recordaremos que era negativo.
    bool es_negativo = false;
    if (n < 0) {
        n *= -1;
        es_negativo = true;
    }

    // Mientras pueda extraer dígitos ...
    string s;
    while (n > 0) {
        // Obtengo el dígito de la unidad.
        int unidad = n % 10;

        // Eliminamos este último dígito.
        n = n / 10;

        // A la cadena le añadimos este dígito al final.
        s += ('0' + unidad);
    }

    // Si el número originalmente era negativo, le añadimos el signo.
    if (es_negativo) {
        s += '-';
    }

    return Revertir(s);
}

int main(void) {
    cout << EnteroACadena(-123) << endl;
    cout << EnteroACadena(0) << endl;
    cout << EnteroACadena(456) << endl;
    return 0;
}