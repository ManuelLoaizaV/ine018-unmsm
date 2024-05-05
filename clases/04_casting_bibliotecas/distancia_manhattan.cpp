#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    // Leemos las coordenadas del taxi.
    int x1, y1;
    cout << "Ingrese las coordenadas del taxi: ";
    cin >> x1 >> y1;

    // Leemos las coordenadas del destino.
    int x2, y2;
    cout << "Ingrese las coordenadas del destino: ";
    cin >> x2 >> y2;

    // Calculamos distancia minima entre las direcciones.
    // Como la ciudad de Manhattan es cuadriculada,
    // solo podemos movernos horizontal y verticalmente.
    int delta_x = abs(x2 - x1);
    int delta_y = abs(y1 - y2);
    int distancia_minima = delta_x + delta_y;
    cout << "El menor numero de cuadras a recorrer es " << distancia_minima << endl;
    return 0;
}