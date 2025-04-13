# Implementado la biblioteca `<cctype>`

En la [clase 4](/clases/04_casting_bibliotecas/)
aprendimos sobre la biblioteca `<cctpe>`
en la cual exportamos muchas funciones que
validan el tipo de dato de un caracter.

```cpp
/*
 * Dígitos: 0123456789
 * Dígitos hexadecimales: 0123456789ABCDEFabcdef
 * Mayúsculas: ABCDEFGHIJKLMNOPQRSTUVWXYZ
 * Minúsculas: abcdefghijklmnopqrstuvwxyz
 * Puntuación: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
 * Espacios:  \t\v\f\n\r
 * Imprimibles: dígitos, mayúsculas, minúsculas, puntuación, espacios.
 */

/* Funciones exportadas */
bool isalnum(char c);
bool isalpha(char c);
bool islower(char c);
bool isupper(char c);
bool isdigit(char c);
bool isxdigit(char c);
bool isspace(char c);
bool isprint(char c);
bool ispunct(char c);
```

Implemente un programa que simule la interfaz de `<cctype>`
usando conjuntos de caracteres.