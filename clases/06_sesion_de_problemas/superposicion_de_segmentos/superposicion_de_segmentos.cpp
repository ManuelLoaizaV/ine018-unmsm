#include <iostream>
using namespace std;

// Retorna si es que [l1, r1] y [l2, r2]
// tienen al menos un punto en común.
bool SuperponenSegmentos(int l1, int r1, int l2, int r2) {
    // Asumiendo que cada segmento es válido (l1 <= r1 y l2 <= r2),
    // es más fácil determinar en qué casos no se intersectan.
    // Así, la respuesta sería la negación de esto.
    return !(r1 < l2 || l1 > r2);
}

int main(void) {
    cout << "[-20, -10] y  [10, 20] se intersectan? " << boolalpha << SuperponenSegmentos(-20, -10, 10, 20) << endl;
    cout << "[0, 10] y [10, 20] se intersectan? " << boolalpha << SuperponenSegmentos(0, 10, 10, 20) << endl;
    cout << "[5, 15] y [10, 20] se intersectan? " << boolalpha << SuperponenSegmentos(5, 15, 10, 20) << endl;
    cout << "[20, 30] y [10, 20] se intersectan? " << boolalpha << SuperponenSegmentos(20, 30, 10, 20) << endl;
    cout << "[30, 40] y [10, 20] se intersectan? " << boolalpha << SuperponenSegmentos(30, 40, 10, 20) << endl;
    return 0;
}