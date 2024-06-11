#include <iostream>
using namespace std;

int CadenaAEntero(string s) {
    // Obtenemos la longitud de la cadena.
    int n = s.size();

    // De izquierda a derecha, construimos el número:
    // Le añadimos un cero a la derecha y le sumamos el dígito actual.
    int entero = 0;

    // Si es que la cadena comienza con un signo -,
    // construimos el número desde el segundo caracter.
    int inicio = 0;
    if (s[0] == '-') {
        inicio = 1;
    }

    // Construimos el valor absoluto del valor numérico
    // representado por la cadena.
    for (int i = inicio; i < n; i++) {
        entero = 10 * entero + (s[i] - '0');
    }

    // Si es que la cadena comenzaba con un signo -,
    // convertimos el valor construido en un número negativo.
    if (s[0] == '-') {
        entero *= -1;
    }

    return entero;
}

int main(void) {
    cout << CadenaAEntero("28") << endl;
    cout << CadenaAEntero("-496") << endl;
    cout << CadenaAEntero("0") << endl;
    cout << CadenaAEntero("8128") << endl;
    cout << CadenaAEntero("-33550336") << endl;
    string a = "-12";
    string b = "34";
    int c = CadenaAEntero(a) + CadenaAEntero(b);
    cout << c << endl;
    return 0;
}