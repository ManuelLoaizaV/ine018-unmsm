#include <iostream>
using namespace std;

bool EsPar(int n) {
    // Caso base: cero es par.
    if (n == 0) {
        return true;
    }
    // Relación de recurrencia: n es par si su predecesor es impar.
    return !EsPar(n - 1);
}

int main(void) {
    cout << EsPar(2) << endl;
    cout << EsPar(7) << endl;
    cout << EsPar(10) << endl;
    cout << EsPar(11) << endl;
    cout << EsPar(312) << endl;
    return 0;
}