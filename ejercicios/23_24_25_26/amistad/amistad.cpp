#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main(void) {
    cout << "Ingrese el número de relaciones amicales: ";
    int n_relaciones;
    cin >> n_relaciones;

    map<string, set<string>> amistades;

    for (int i = 1; i <= n_relaciones; i++) {
        cout << "(" << i << ") Ingrese el nombre de las dos personas relacionadas: ";
        string s, t;
        cin >> s >> t;

        if (!amistades.contains(s)) {
            amistades[s] = set<string>();
        }
        amistades[s].insert(t);

        if (!amistades.contains(t)) {
            amistades[t] = set<string>();
        }
        amistades[t].insert(s);
    }

    cout << "Ingrese el número de consultas: ";
    int n_consultas;
    cin >> n_consultas;
    for (int i = 1; i <= n_consultas; i++) {
        cout << "(" << i << ") Ingrese la persona a consultar: ";
        string nombre;
        cin >> nombre;

        if (amistades.contains(nombre)) {
            cout << "Amistades de " << nombre << ":";
            for (string amistad : amistades[nombre]) {
                cout << " " << amistad;
            }
            cout << endl;
        } else {
            cout << nombre << " no está en la lista de matriculados" << endl;
        }
    }
    return 0;
}