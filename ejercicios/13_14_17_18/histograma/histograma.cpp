#include <iostream>
#include <vector>

using namespace std;

// Hoja de ruta
// 1. Consultar y leer el número de alumnos.
// 2. Consultar y leer la nota de todos los alumnos.
// 3. Imprimir histograma.
//   i. Crear vector que represente los "cajones". Recuerde que estamos contando.
//   ii. Iterar el vector de notas y para cada nota, sumar 1 en el cajón respectivo.
//   iii. Iterar el vector de cajones, y para cada número par imprimir lo siguiente:
//   - Imprimir el número del cajón con el formato adecuado (04, 16, ...).
//   - Imprimir tantos asteriscos como frecuencia en el cajón actual.

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
    cout << "Ingrese el número de alumnos: ";
    int n;
    cin >> n;

    vector<int> notas;
    for (int i = 1; i <= n; i++) {
        cout << "Ingrese la nota del alumno " << i << ": ";
        int nota;
        cin >> nota;
        notas.push_back(nota);
    }

    vector<int> cajones(21, 0);
    for (int i = 0; i < n; i++) {
        if (notas[i] % 2 == 0) {
            cajones[notas[i]]++;
        } else {
            cajones[notas[i] - 1]++;
        }
    }

    for (int i = 0; i <= 20; i += 2) {
        if (i < 10) {
            cout << 0;
        }
        cout << i << ": ";
        for (int j = 0; j < cajones[i]; j++) {
            cout << '*';
        }
        cout << endl;
    }
    return 0;
}
