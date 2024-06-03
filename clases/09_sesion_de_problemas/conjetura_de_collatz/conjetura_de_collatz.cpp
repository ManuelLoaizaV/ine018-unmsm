#include <iostream>
using namespace std;

int main(void) {
    int n = 27;
    int pasos = 0;

    int original = n;

    while (n > 1) {
        int m = 0;
        if (n % 2 == 0) {
            m = n / 2;
            cout << n << " es par, entonces tomo la mitad: " << m << endl;
        } else {
            m = 3 * n + 1;
            cout << n << " es impar, entonces hago 3n + 1: " << m << endl;
        }
        n = m;
        pasos++;
    }

    cout << "Wow, fue un viaje de " << pasos << " paso(s) desde " << original << " hasta 1.";
    cout <<  " Pero al final llegue. Eso quiere decir que " << original << " es maravilloso.";
    cout << " Me pregunto que numeros no seran maravillosos ..." << endl;;
    return 0;
}