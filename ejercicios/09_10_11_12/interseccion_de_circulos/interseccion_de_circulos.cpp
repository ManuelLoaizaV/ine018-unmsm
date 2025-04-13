#include <iostream>
#include <cmath>
using namespace std;

long double Distancia(long double x1, long double y1, long double x2, long double y2) {
    long double dx = x2 - x1;
    long double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

bool IntersectanCirculos(
    double x1, double y1, double r1,
    double x2, double y2, double r2
) {
    return Distancia(x1, y1, x2, y2) <= r1 + r2;
}

int main(void) {
    cout << IntersectanCirculos(0, 0, 5, 0, 6, 2) << endl;
    cout << IntersectanCirculos(0, 0, 10, 50, 50, 10) << endl;
    return 0;
}