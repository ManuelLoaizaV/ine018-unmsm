## Tipos fundamentales
```cpp
int siete = 7;  // Entero con signo de 32 bits (usualmente)
char efe = 'F';  // Caracter ASCII de 8 bits (usualmente)
float pi = 3.1415;  // Número de punto flotante de precisión simple de 32 bits (usualmente)
double e = 2.718281828459;  // Número de punto flotante con precisión doble de 64 bits (usualmente)
bool verdad = true;  // 1 bit

#include <string>
std::str curso = "INE018";  // Cadena de caracteres
```

¿Qué tipos de datos son los siguientes?

```cpp
auto a = "test";
auto b = 3.2 * 5 - 1;
auto c = 5 / 2;

auto d(int x) { return x / 2; }
auto e(double x) { return x / 2; }
auto f(double x) { return int(x / 2); }

auto g(double x) {
    std::cout << x << std::endl;
}
```

### ¡C++ es un lenguaje de tipado estático!

**Tipado estático**:
todo lo que tiene nombre
(variables, funciones, etc.)
requiere un tipo antes del tiempo de ejecución.

Un lenguaje de programación como Python
es de **tipado dinámico**:
todo lo que tiene nombre
(variables, funciones, etc.)
obtiene un tipo en tiempo de ejecución
dependiendo del valor actual del individuo en cuestión.

**Tiempo de ejecución**:
Periodo en el que un programa está ejecutando comandos
(luego de la compilación, en caso hayamos compilado).

#### Tipado dinámico, interpretado
- Los tipos se verifican sobre la marcha,
durante la ejecución,
línea por línea.
- Ejemplos: Python, JavaScript, PHP.

#### Tipado estático, compilado
- Los tipos tienen que estar definidos
antes que se ejecute el programa
durante compilación.
- Ejemplos: C++, Go, Rust.

#### Tipado dinámico versus tipado estático

En Python, las variables pueden cambiar de tipo durante la ejecución del programa.
Por ejemplo:

```python
numero = 5
mensaje = "hola"
numero = 10
mensaje = 42
```

Aquí, `mensaje` comienza como una cadena y luego se cambia a un número. Python permite este tipo de flexibilidad.

Por otro lado, en C++, el tipado es estático,
lo que significa que el tipo de una variable se determina en tiempo de compilación y no puede cambiar.
Por lo tanto, el siguiente código en C++ dará un error de compilación:

```cpp
int numero = 5;
string mensaje = "hola";
numero = 10;
mensaje = 42;  // ERROR
```

Aquí, `mensaje` se declara como una cadena,
por lo que no se puede asignar un entero directamente a ella.

Además, la diferencia en el manejo de tipos se extiende a las funciones. En Python, las funciones pueden manejar tipos dinámicos:

```python
def triplicar(x):
    return x * 3

triplicar("42")
```
Esto devolverá `"424242"`, ya que Python permite multiplicar cadenas por un entero para repetirlas.


En contraste, en C++,
las funciones esperan tipos específicos y el compilador
verificará esto en tiempo de compilación:

```cpp
int triplicar(int x) {
    return x * 3;
}

triplicar("42");  // ERROR
```

Aquí, la función triplicar está diseñada para operar con enteros,
por lo que pasar una cadena resultará en un error de compilación,
ya que el tipo esperado no coincide con el proporcionado.

## Variables

Una **declaración de variable** es una sentencia en la cual
creamos una nueva variable y le asignamos un tipo de dato.
La sintaxis para ello es la siguiente:

```cpp
TIPO_DE_DATO NOMBRE_DE_LA_VARIABLE;
```

Note que podemos combinar literales con variables en nuestras sentencias `cout`:

```cpp
int x = 18;
string curso = "Matematica computacional";
cout << "INE" << 0 << x << " " << curso << " es interesante." << endl;
```

### Errores comunes con variables

#### Variable no declarada
```cpp
#include <iostream>
using namespace std;
int main(void) {
    x = 2;  // ERROR: x no está declarada
    cout << x << endl;
    return 0;
}
```

#### Incompatibilidad de tipos
```cpp
#include <iostream>
using namespace std;
int main(void) {
    int x = 2;
    x = "hola";  // ERROR: x puede almacenar un entero, no una cadena
    cout << x << endl;
    return 0;
}
```

#### Intento de cambiar el tipo de dato de una variable
```cpp
#include <iostream>
using namespace std;
int main(void) {
    int x = 2;
    string x = "hola";  // ERROR: x ya está declarada
    cout << x << endl;
    return 0;
}
```

#### Redeclaración de una variable
```cpp
#include <iostream>
using namespace std;
int main(void) {
    int x = 2;
    int x = 3;  // ERROR: x ya está declarada
    cout << x << endl;
    return 0;
}
```


### Variables no inicializadas

En C++, las variables no se inicializan automáticamente.
Por defecto, si no asignas un valor a una variable,
la variable contiene cualquier basura que se encuentre en la dirección de memoria asignada.

> [!NOTE]
> Las variables de tipo `string` serían una excepción
> puesto que están vacías por defecto.

La mayoría de los compiladores de C++
permitirán compilar código en el que las variables no han sido inicializadas.
Otros compiladores inicializan los direcciones de memoria de las variables
con un valor predefinido. 

```cpp
#include <iostream>
using namespace std;
int main(void) {
    int x;
    int y;
    int z;
    // Imprimamos variables no inicializadas D:
    cout << x << " " << y << " " << z << endl;
    return 0;
}
```

## Operadores

### Operadores de comparación

| Operador | Significado           |
|----------|-------------------|
| `<` | menor que |
| `<=` | menor o igual que |
| `>` | mayor que |
| `>=` | mayor o igual que |
| `==` | igual a |
| `!=` | distinto a |

Ten en cuenta que el operador `<=`
no puede escribirse como `=<`.
Lo mismo ocurre con el operador `>=`.
Una forma de recordar esto es que es mucho más común decir
"menor o igual que" en español que
"igual o menor que".

### Operadores booleanos

| Operador | Significado |
|---|---|
| `!` | negación |
| `&&` | Y lógico |
| `\|\|` | O lógico |

> [!WARNING]
> Debes usar dos signos et para el operador `&&` y
> dos plecas para el operador `||`.
> Si solo usas un `&` o un `|`,
> obtendrás una operación diferente (a nivel de bits).

## Expresiones

Una expresión es una sucesión de operadores y sus operandos que especifican computar algo.

Evaluar una expresión puede producir un resultado o generar efectos secundarios.

### Precedencia
1. Negación.
2. Paréntesis.
3. Multiplicación, módulo, división.
4. Adición, concatenación, substracción.
5. Operadores de comparación.
6. Operadores de igualdad.
7. Y lógico.
8. O lógico.

### Practiquemos

```cpp
1 + 2 * 3
```

```cpp
(1 + 2) * 3
```

```cpp
5 + 2 * 4
```

```cpp
1 + 2 / 3
```

```cpp
6 * 5 % 7
```

```cpp
5 * 3 + 1.0
```

```cpp
8 / 3 * 2.0
```

```cpp
8.0 / 3 * 2
```

```cpp
"Hola" + "mundo"
```

```cpp
1 + 2 * 3 != (1 + 2) * 3
```

```cpp
5 * 3 < 12
```

```cpp
10 % 3 == 10 / 3
```

```cpp
5 < 9 || (7 != 7)
```

```cpp
!(1 + 2 == 3 && 10 % 4 > 2)
```

```cpp
int i = 2;
int j = 3;
int k = 4;
int x = i + j + k;
i = x - i - j;
j = x - j - k;
k = x - i - k;

cout << i << " " << j << " " << k << endl;
```

```cpp
int a = 5;
int b = 10;
int c = b;

a = a + 1;
b = b - 1;
c = c + a;

cout << a << " " << b << " " << c << endl;
```