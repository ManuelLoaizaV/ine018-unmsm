#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
    // Leemos las coordenadas del primer punto.
    double x1, y1, z1;
    cout << "Ingrese las coordenadas del primer punto: ";
    cin >> x1 >> y1 >> z1;

    // Leemos las coordenadas del segundo punto.
    double x2, y2, z2;
    cout << "Ingrese las coordenadas del segundo punto: ";
    cin >> x2 >> y2 >> z2;

    // Calculamos e imprimios la distancia euclideana entre estos puntos.
    double delta_x = x1 - x2;
    double delta_y = y1 - y2;
    double delta_z = z1 - z2;
    double distancia = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z);
    cout << "La distancia entre los dos puntos es " << distancia << endl;
    return 0;
}
