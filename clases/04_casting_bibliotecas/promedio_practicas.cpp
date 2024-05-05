#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;

int main(void) {
    // Leemos las notas de las prácticas calificadas.
    int pc1, pc2, pc3, pc4;
    cout << "Ingrese las cuatro notas de sus practicas calificadas: ";
    cin >> pc1 >> pc2 >> pc3 >> pc4;

    // Obtenemos la menor de las notas para poder eliminarla.
    int minima_pc = min(pc1, min(pc2, min(pc3, pc4)));

    // Calculamos e imprimimos el promedio practicas calificadas.
    // Notar que el numerador es entero y el denominador punto flotante.
    double promedio = (pc1 + pc2 + pc3 + pc4 - minima_pc) / 3.0;
    cout << "El promedio de practicas es " << fixed << setprecision(2) << promedio << endl;
    return 0;
}