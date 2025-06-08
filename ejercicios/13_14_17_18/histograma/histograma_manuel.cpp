#include <iostream>
#include <vector>

using namespace std;

// Hoja de ruta
// 1. Consultar y leer el número de alumnos.
// 2. Consultar y leer la nota de todos los alumnos.
// 3. Imprimir histograma.

// Ejemplo
// Ingrese el número de alumnos: 12
// Ingrese la nota del alumno 1: 20
// Ingrese la nota del alumno 2: 19
// ...
// Ingrese la nota del alumnos 12: 16
// 00:
// 02:
// 04:
// 06:
// 08: *
// 10: *
// 12:
// 14: **
// 16: *****
// 18: **
// 20: *

int main(void) {
    cout << "Ingrese la cantidad de alumnos: ";
    int n;
    cin >> n;
    
    vector<int> frecuencias(22, 0);
    for (int i = 1; i <= n; i++) {
        cout << "Ingrese la nota del alumno " << i  << ": ";
        int nota;
        cin >> nota;
        frecuencias[nota]++;
    }

    for (int i = 0; i <= 20; i += 2) {
        if (i < 10) cout << 0;
        cout << i << ": ";
        int cnt = frecuencias[i] + frecuencias[i + 1];
        for (int j = 0; j < cnt; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
