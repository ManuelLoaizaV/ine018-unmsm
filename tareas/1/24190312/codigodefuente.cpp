#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Ingrese un número entero positivo: ";
    cin >> n;

    int suma = 0;
    for(int i = 1; i <= n; ++i) {
        suma += i;
    }

cout << "La suma de los primeros " << n << " números naturales es: " << suma << endl;

    return 0;
}