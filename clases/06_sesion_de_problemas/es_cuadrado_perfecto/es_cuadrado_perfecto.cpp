#include <iostream>
#include <cmath>
using namespace std;

bool EsCuadradoPerfecto(int n) {
    if (n < 0) {
        return false;
    }
    int raiz = sqrt(n);
    return raiz * raiz == n;
}

int main(void) {
    cout << EsCuadradoPerfecto(-42) << endl;
    cout << EsCuadradoPerfecto(0) << endl;
    cout << EsCuadradoPerfecto(1) << endl;
    cout << EsCuadradoPerfecto(5) << endl;
    cout << EsCuadradoPerfecto(9) << endl;
    cout << EsCuadradoPerfecto(99) << endl;
    return 0;
}