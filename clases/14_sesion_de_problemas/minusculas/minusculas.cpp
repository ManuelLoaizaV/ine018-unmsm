#include <iostream>
using namespace std;

string Minusculas(string s) {
    // Obtenemos el tamaño de la cadena
    int n = s.size();

    // Para cada caracter de la cadena
    for (int i = 0; i < n; i++) {
        // Si es que este es mayúscula, lo convertimos a minúscula
        if ('A' <= s[i] && s[i] <= 'Z') {
            s[i] = (s[i] - 'A') + 'a';
        }
    }

    // Finalmente, retornamos la cadena modificada
    return s;
}

int main(void) {
    cout << Minusculas("Manuel Loaiza") << endl;
    cout << Minusculas("alex cisneros") << endl;
    cout << Minusculas("ARIADNA ROSSA") << endl;
    cout << Minusculas("pi=3.1415926535897932") << endl;
    string s = "UnMsm2024";
    cout << Minusculas(s) << endl;
    return 0;
}