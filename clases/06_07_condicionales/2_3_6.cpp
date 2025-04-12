#include <iostream>
using namespace std;

int main(void) {
    cout << "Ingrese un numero entero: ";
    int n;
    cin >> n;

    if (n % 6 == 0) {
        cout << n << " es multiplo de 6" << endl;
    } else {
        if (n % 2 == 0) {
            cout << n << " es par" << endl;
        }
        if (n % 3 == 0) {
            cout << n << " es multiplo de 3" << endl;
        }
    }

    return 0;
}
