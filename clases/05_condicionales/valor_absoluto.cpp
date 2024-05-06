#include <iostream>
using namespace std;

int main(void) {
    // Leemos la entrada del usuario.
    int n;
    cout << "Ingrese un numero entero: ";
    cin >> n;

    // Por defecto, asumamos que el valor absoluto del numero
    // coincide con el número ingresado.
    int valor_absoluto = n;
    
    // En caso el número sea negativo, cambiamos el signo del resultado.
    if (n < 0) {
        // Recuerden que *= es equivalente a lo siguiente:
        // valor_absoluto = valor_absoluto * -1;
        // Pueden leer más en la documentación:
        // https://en.cppreference.com/w/cpp/language/operator_assignment
        valor_absoluto *= -1;
    }

    cout << "El valor absoluto de " << n << " es " << valor_absoluto << endl;
    return 0;
}