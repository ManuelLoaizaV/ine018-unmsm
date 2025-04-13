#include <iostream>
#include <cstdlib>
using namespace std;

int ObtenerDocenasDeHuevos(int huevos) {
    int docenas = huevos / 12;
    if (huevos % 12 > 0) {
        docenas++;
    }
    return docenas;
}

int main(void) {
    for (int i = 0; i < 10; i++) {
        int huevos = 1 + rand() % 100;
        cout << "Huevos: " << huevos;
        cout << " Docenas: " << ObtenerDocenasDeHuevos(huevos) << endl;
    }
}