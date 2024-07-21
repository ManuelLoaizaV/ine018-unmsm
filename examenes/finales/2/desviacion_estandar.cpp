#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

long double Media(const vector<long double>& datos) {
    long double suma = 0.0L;
    for (long double dato : datos) suma += dato;
    return suma / datos.size();
}

long double DesviacionEstandar(const vector<long double>& datos) {
    long double media = Media(datos);
    long double suma = 0.0L;
    for (long double dato : datos) {
        long double delta = media - dato;
        suma += delta * delta;
    }
    return sqrt(suma) / datos.size();
}

int main(void) {
    vector<long double> v = {14.0L, 15.0L, 19.0L, 20.0L, 20.0L};
    cout << DesviacionEstandar(v) << endl;
    return 0;
}