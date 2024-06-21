#include <iostream>

int main() {
    // Declaración de variables
    int num1, num2, suma;

    // Solicitar al usuario que ingrese el primer número
    std::cout << "Ingrese el primer número: ";
    std::cin >> num1;

    // Solicitar al usuario que ingrese el segundo número
    std::cout << "Ingrese el segundo número: ";
    std::cin >> num2;

    // Sumar los dos números
    suma = num1 + num2;

    // Mostrar el resultado
    std::cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << std::endl;

    return 0;
}
