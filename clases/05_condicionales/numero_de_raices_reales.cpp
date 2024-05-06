#include <iostream>
using namespace std;

// Retorna el número de raíces reales que tiene
// la ecuación ax^2 + bx + c = 0.
int NumeroDeRaicesReales(int a, int b, int c) {
    // Calculamos Δ = b^2 - 4ac.
    int discriminante = b * b - 4 * a * c;

    // Inicialicemos nuestra variable asumiendo que no existen raíces reales.
    int numero_de_raices = 0;

    // Si Δ > 0, tenemos dos raíces reales y diferentes:
    // x1 = (-b - √Δ) / 2a,
    // x2 = (-b + √Δ) / 2a.
    if (discriminante > 0) {
        numero_de_raices = 2;
    } else if (discriminante == 0) {
        // Si Δ = 0, tenemos una raíz real:
        // x = -b / 2a
        numero_de_raices = 1;
    }

    // Si Δ < 0, ambas raíces son complejas con parte imaginaria no nula.
    // Como nuestra variable la habíamos inicializado en cero,
    // no hay que realizar ninguna modificación.

    return numero_de_raices;
}

int main(void) {
    cout << "4x^2 + 5x + 1 = 0 tiene " << NumeroDeRaicesReales(4,5,1) << " raices." << endl;
    cout << "4x^2 + 4x + 1 = 0 tiene " << NumeroDeRaicesReales(4,4,1) << " raices." << endl;
    cout << "4x^2 + 3x + 1 = 0 tiene " << NumeroDeRaicesReales(4,3,1) << " raices." << endl;
    return 0;    
}