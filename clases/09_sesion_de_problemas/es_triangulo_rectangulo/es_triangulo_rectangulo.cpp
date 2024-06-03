#include <iostream>
#include <cmath>
using namespace std;

long double Distancia(long double x1, long double y1, long double x2, long double y2) {
    long double dx = x2 - x1;
    long double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

bool EsTrianguloRectangulo(
    long double x1, long double y1,
    long double x2, long double y2,
    long double x3, long double y3
) {
    long double a = Distancia(x1, y1, x2, y2);
    long double b = Distancia(x1, y1, x3, y3);
    long double c = Distancia(x2, y2, x3, y3);

    return a * a + b * b == c * c ||
    a * a + c * c == b * b ||
    c * c + b * b == a * a;
}

int main(void) {
    cout << EsTrianguloRectangulo(0, 0, 0, 3, 4, 0) << endl;
    cout << EsTrianguloRectangulo(0, 0, 0, 3, 4, 1) << endl;
    return 0;
}