#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>

int main(void) {
    // Un entero usualmente ocupa 32 bits.
    // Los valores van de [-2^31, 2^31).
    // Representados en complemento a 2.
    // Es decir,
    //  0: 000  1: 001  2: 010  3: 011
    // -4: 100 -1: 111 -2: 110 -3: 101
    short corto = 3;
    std::cout << "El menor numero primo impar es " << corto << "." << std::endl;
    std::cout << "Un short ocupa " << sizeof(short) << " bytes." << std::endl;

    int entero = 34631367;
    std::cout << "Peru tiene " << entero << " habitantes." << std::endl;
    std::cout << "Un int ocupa " << sizeof(int) << " bytes." << std::endl;

    long long largo = 2831732137780LL;
    std::cout << "El market cap de Apple es " << largo << " comenzando el 2024." << std::endl;
    std::cout << "Un long long ocupa " << sizeof(long long) << " bytes." << std::endl;

    // Un caracter usualmente ocupa 8 bits.
    // Los valores siguen la codificacion UTF-8.
    // Los primeros 2^7 = 128 códigos coinciden con ASCII.
    char caracter = 'A';
    char otro_caracter = 66;
    std::cout << "Las dos primeras letras del alfabeto son ";
    std::cout << caracter << " y " << otro_caracter << "." << std::endl;
    std::cout << "Un caracter ocupa " << sizeof(char) << " bytes." << std::endl;

    // Tipo de punto flotante con precisión simple.
    // Utiliza IEEE-754 binary32 format.
    float simple = acosf(-1.0F);
    std::cout << "float PI: " << std::fixed << std::setprecision(23) << simple << std::endl;
    std::cout << "Un float ocupa " << sizeof(float) << " bytes." << std::endl;

    // Tipo de punto flotante con precisión doble.
    // Utiliza IEEE-754 binary64 format.
    double doble = acos(-1.0);
    std::cout << "double PI: " << std::fixed << std::setprecision(49) << doble << std::endl;
    std::cout << "Un double ocupa " << sizeof(double) << " bytes." << std::endl;

    long double extendido = acosl(-1.0L);
    std::cout << "long double PI: " << std::fixed << std::setprecision(63) << extendido << std::endl;
    std::cout << "Un long double ocupa " << sizeof(long double) << " bytes." << std::endl;

    bool falso = false;
    std::cout << "La tierra es plana? " << std::boolalpha << falso << std::endl;
    bool verdad = true;
    std::cout << "Todos somos mortales? " << std::boolalpha << verdad << std::endl;
    // A pesar de que un booleano deberia ocupar un bit,
    // la menor unidad para reservar memoria en C++ es el byte.
    std::cout << "Un bool ocupa " << sizeof(bool) << " bytes." << std::endl;

    // El tipo de dato string no viene integrado en C++,
    // por lo que tenemos que importar la biblioteca <string>.
    std::string nombre = "Manuel";
    std::cout << "Mi nombre es " << nombre << "." << std::endl;
    return 0;
}