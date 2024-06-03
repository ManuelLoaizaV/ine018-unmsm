#include <iostream>
using namespace std;

string Mayusculas(string s) {
    // Obtenemos el tamaño de la cadena
    int n = s.size();

    // Para cada caracter de la cadena
    for (int i = 0; i < n; i++) {
        // Si es que este es minúscula, lo convertimos a mayúscula
        if ('a' <= s[i] && s[i] <= 'z') {
            s[i] = (s[i] - 'a') + 'A';
        }
    }

    // Finalmente, retornamos la cadena modificada
    return s;
}

int main(void) {
    cout << Mayusculas("Manuel Loaiza") << endl;
    cout << Mayusculas("alex cisneros") << endl;
    cout << Mayusculas("ARIADNA ROSSA") << endl;
    cout << Mayusculas("pi=3.1415926535897932") << endl;
    string s = "UnMsm2024";
    cout << Mayusculas(s) << endl;
    return 0;
}