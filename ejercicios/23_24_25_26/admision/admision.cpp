#include <iostream>
#include <map>

using namespace std;

int main(void) {
    cout << "Ingrese el número de ingresantes: ";
    int n;
    cin >> n;

    map<string, int> frecuencias;

    for (int i = 1; i <= n; i++) {
        cout << "(" << i << ") Ingrese el nombre del cachimbo: ";
        string nombre;
        cin >> nombre;

        if (frecuencias.contains(nombre)) {
            cout << nombre << frecuencias[nombre] << "@unmsm.edu.pe" << endl;
            frecuencias[nombre]++;

        } else {
            cout << nombre << "@unmsm.edu.pe" << endl;
            frecuencias[nombre] = 1;
        }
    }
    return 0;   
}
