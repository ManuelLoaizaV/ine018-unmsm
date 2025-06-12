// Ejercicio 1
// Solicitar los dígitos de su código estudiantil.
// Solicitar el nombre del alumno.
// Imprimir en orden creciente los dígitos únicos de su código
// y letras únicas de su nombre.

// Input:
// 2 0 1 8 5 0 4 8
// alejandro

// Output
// 0 1 2 4 5 8
// a d e j l n o

#include <iostream>
#include <set>
using namespace std;

int main(void) {
    int n;
    cout << "Ingrese el número de dígitos de su código estudiantil: ";
    cin >> n;
    set<int> digitos;
    for (int i = 1; i <= n; i++) {
        cout << "Ingrese el dígito " << i << ": ";
        int d;
        cin >> d;
        digitos.insert(d);
    }

    cout << "Ingrese su nombre: ";
    string nombre;
    cin >> nombre;
    set<char> caracteres;
    for (char c : nombre) {
        caracteres.insert(c);
    }

    for (int digito : digitos) {
        cout << digito << ' ';
    }
    cout << endl;
    for (char caracter : caracteres) {
        cout << caracter << ' ';
    }
    cout << endl;
    return 0;
}