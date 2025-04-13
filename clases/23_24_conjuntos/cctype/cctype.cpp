#include <iostream>
#include <set>
using namespace std;

set<char> digitos;
set<char> hexadecimales;
set<char> mayusculas;
set<char> minusculas;
set<char> puntuacion;
set<char> espacios;

bool islower(char c) {
    return minusculas.contains(c);
}
bool isupper(char c) {
    return mayusculas.contains(c);
}
bool isalpha(char c) {
    return islower(c) || isupper(c);
}
bool isdigit(char c) {
    return digitos.contains(c);
}
bool isalnum(char c) {
    return isalpha(c) || isdigit(c);
}
bool isxdigit(char c) {
    return hexadecimales.contains(c);
}
bool isspace(char c) {
    return espacios.contains(c);
}
bool ispunct(char c) {
    return puntuacion.contains(c);
}
bool isprint(char c) {
    return isdigit(c) || isupper(c) || islower(c) || ispunct(c) || isspace(c);
}

int main(void) {
    for (char c = '0'; c <= '9'; c++) {
        digitos.insert(c);
        hexadecimales.insert(c);
    }
    for (char c = 'a'; c <= 'z'; c++) {
        minusculas.insert(c);
        if (c <= 'e') {
            hexadecimales.insert(c);
        }
    }
    for (char c = 'A'; c <= 'Z'; c++) {
        mayusculas.insert(c);
        if (c <= 'E') {
            hexadecimales.insert(c);
        }
    }
    string cadena_de_espacios = " \t\v\f\n\r";
    for (char c : cadena_de_espacios) {
        espacios.insert(c);
    }
    string cadena_de_puntuaciones = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    for (char c : cadena_de_puntuaciones) {
        puntuacion.insert(c);
    }

    cout << islower('a');
    cout << islower('z');
    cout << islower('F');
    cout << islower('#');
    cout << endl;

    cout << isupper('A');
    cout << isupper('B');
    cout << isupper('f');
    cout << isupper('%');
    cout << endl;

    cout << isalpha('a');
    cout << isalpha('B');
    cout << isalpha('3');
    cout << isalpha('$');
    cout << endl;

    cout << isdigit('0');
    cout << isdigit('9');
    cout << isdigit('a');
    cout << isdigit('*');
    cout << endl;

    cout << ispunct('@');
    cout << ispunct('#');
    cout << ispunct('2');
    cout << ispunct('u');
    cout << endl;

    cout << isalnum('x');
    cout << isalnum('E');
    cout << isalnum('5');
    cout << isalnum('+');
    cout << isalnum('\n');
    cout << endl;

    cout << isxdigit('4');
    cout << isxdigit('b');
    cout << isxdigit('D');
    cout << isxdigit('g');
    cout << isxdigit('H');
    cout << isxdigit('?');
    cout << endl;

    cout << isspace(' ');
    cout << isspace('\t');
    cout << isspace('\n');
    cout << isspace('L');
    cout << isspace('m');
    cout << isspace('7');
    cout << endl;

    cout << isprint('m');
    cout << isprint('N');
    cout << isprint('8');
    cout << isprint('!');
    cout << isprint(' ');
    cout << isprint('\0');
    cout << isprint(7);
    cout << isprint(15);
    cout << isprint(31);
    cout << isprint(127);
    cout << endl;

    return 0;
}
