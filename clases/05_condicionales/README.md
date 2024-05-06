## Bloques

En C++ está definido que las sentencias de control se aplican a sentencias simples.
Cuando estás escribiendo un programa,
normalmente quieres que una sentencia de control aplique
a un conjunto de sentencias.
Para indicar que una sucesión de sentencias forman una unidad coherente,
agrupamos todas estas sentencias en un **bloque**,
el cual es una colección de sentencias rodeadas por llaves:

```cpp
{
    sentencia_1;
    sentencia_2;
    ...
    sentencia_n;
}
```

Cuando el compilador de C++ encuentra un bloque,
este trata el bloque entero como si fuese una sola sentencia.

## La sentencia `if`

Cuando escribimos un programa,
solemos querer verificar cierta condición
para controlar lo que el programa ejecutará posteriormente.
A este tipo de control de un programa se le conoce
como **ejecución condicional**.

La manera más fácil de expresar ejecución condicional en C++
es utilizando la sentencia `if`.

La primera forma de la sentencia `if`
ocurre cuando tu estrategia llama a un conjunto de sentencias a ser ejecutadas
solo si una determinada condición booleana es `true`.
Si la condición es `false`, estas sentencias son simplemente ignoradas.

```
if (condicion) sentencia
```

La segunda forma de la sentencia `if` se utiliza cuando
el programa tiene que decidir entre dos conjuntos independientes de sentencias
basado en el resultado de cierta condición.

```
if (condicion) sentencia else sentencia
```

Por ejemplo, el siguiente programa imprime si
un número entero `n` es par o impar.

```cpp
if (n % 2 == 0) {
    cout << n << " es par." << endl;
} else {
    cout << n << "es impar." << endl;
}
```

## La sentencia `switch`

La sentencia `if` era perfecta
cuando la lógica de nuestro tenía dos rutas dependiendo de una condición.
Sin embargo, a veces tenemos que tomar decisiones
con más casos mutuamente excluyentes.

Una manera de lidiar con esto sin anidar sentencias `if`
es utilizar la sentencia `switch`, la cual tiene la siguiente sintaxis:

```
switch (e) {
    case c1:
        statements;
        break;
    case c2:
        statements;
        break;
    ...
    case cn:
        statements;
        break;
    default:
        statements;
        break;
}
```

La expresión de control, `e`,
es comparada contra las constantes
`c1` hasta `cn`.
Si una constante coincide con la expresión,
las sentencias asociadas a dicho `case` son ejecutadas.
Opcionalmente, uno puede definir con `default`
una sección que se ejecute si es que nuestro programa llegó hasta dicho punto.

```cpp
bool EsVocal(char c) {
    switch (c) {
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            return true;
        default:
            return false;
    }
}
```

Si es que el programa ejecuta alguna sentencia `break`,
el programa continúa con la sentencia luego de todo el `switch`.

```cpp
switch(operacion) {
    case '+':
        cout << "Suma" << endl;
        break;
    case '-':
        cout << "Resta" << endl;
        break;
    case '*':
        cout << "Multiplicacion" << endl;
        break;
    case '/':
        cout << "Division" << endl;
        break;
    default:
        cout << "La operacion no es ninguna de [+, -, *, /]." << endl;
        break;
}
```
