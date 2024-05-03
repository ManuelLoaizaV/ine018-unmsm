## Casting

C++ te permite realizar conversiones entre tipos.
A veces esto ocurre automáticamente. Por ejemplo,
```cpp
int entero = 3;
float real = entero;
```
funciona sin problemas porque ocurrió un casting implícito.
Esto también permite hacer
```cpp
float real = 3.14;
int entero = real;
```
a pesar de que un entero no pueda almacenar el valor `3.14`.

A veces C++ solo te permitirá realizar la conversión si explíticamente lo solicitas.
Para esto tenemos cuatro operadores:
`const_cast`,
`static_cast`,
`dynamic_cast`
y `reinterpret_cast`.

## Bibliotecas

La mayoría del código que nuestra computadora ejecuta
no es el que hemos escrito, sino el código de una biblioteca
que hemos importado en nuestro programa.

En las clases anteriores hemos utilizado la biblioteca
`<iostream>` para poder acceder a los streams `cin` y `cout`.
Los detalles de implementación de estos streams
no son importantes a la hora de escribir nuestro primer `Hola, mundo!`.
Como ingenieros, lo que nos importa es saber cómo usar estas bibliotecas
y que la implementación de estas hacen lo que deberían hacer.

Para muchos principiantes la idea de utilizar una función
sin entender cómo fue implementada puede ser incómoda.
Sin embargo, ustedes han estado haciendo esto en el colegio desde hace muchos años.
Ustedes aprendieron sobre logaritmos, senos y cosenos
memorizando ciertos valores sin tener que computarlos manualmente
ni tener que saber sobre funciones analíticas u holomorfas.
A la hora de programar, seguiremos la misma estrategia que en el colegio.

### `<cmath>`

C++ nos provee una biblioteca matemática bastante rica.
Podemos encontrar funciones matemáticas generales:

| Función | Descripción |
|---|---|
| `abs(x)` | Retorna el valor absoluto de $x$.  |
| `sqrt(x)` | Retorna la raíz cuadra de $x$. |
| `floor(x)` | Retorna el máximo entero menor o igual a $x$. |
| `ceil(x)` | Retorna el mínimo entero mayor o igual a $x$. |

Funciones matemáticas logarítmicas y exponenciales:

| Función | Descripción |
|---|---|
| `exp(x)` | Retorna el valor de $e^x$.  |
| `log(x)` | Retorna la logaritmo natural de $x$. |
| `log10(x)` | Retorna el logaritmo en base $10$ de $x$. |
| `pow(x, y)` | Retorna $x^y$. |

Funciones trigonométricas:

| Función | Descripción |
|---|---|
| `cos(x)` | Retorna el coseno del ángulo $x$ medido en radianes antihorariamente desde el eje $+x$. |
| `sin(x)` | Retorna el seno de $x$ radianes. |
| `tan(x)` | Retorna la tangente de $x$ radianes. |
| `atan(x)` | Retorna $x^y$. |
| `atan2(y, x)` | Retorna el ángulo en radianes formado entre el eje $x$ y el segmento que une el origen con $(x, y)$. |

### `<algorithm>`

Esta biblioteca define funciones para
búsquedas,
ordenamientos,
conteos
y otras cosas más.

| Función | Descripción |
|---|---|
| `find` | Encuentra el primer elemento que satisface cierto criterio. |
| `swap` | Intercambia los valores de dos objetos. |
| `fill` | Asigna el valor especificado a cada elemento en el rango dado. |
| `reverse` | Invierte el orden de los elementos en un rango. |
| `sample` | Selecciona $n$ elementos aleatoriamente de una sucesión. |
| `sort` | Ordena un rango ascendentemente. |
| `lower_bound` | Retorna el iterador al primer elemento que no es menor que un valor. |
| `upper_bound` | Retorna el iterador al primer elemento que es mayor que un valor. |
| `max` | Retorna el máximo de los valores dados. |
| `min` | Retorna el mínimo de los valores dados. |

### `<cstdlib>`

| Función | Descripción |
|---|---|
| `atof` | Convierte una cadena en un `double`. |
| `atoi` | Convierte una cadena en un `int`. |
| `rand` | Genera un número aleatorio. |

### `<cctype>`

| Función | Descripción |
|---|---|
| `isalnum` | Valida que un caracter sea alfanumérico. |
| `isalpha` | Valida que un caracter sea una letra del abecedario. |
| `isdigit` | Valida que un caracter sea un dígito decimal. |
| `islower` | Valida que un caracter esté en minúscula. |
| `isupper` | Valida que un caracter esté en mayúscula. |
| `tolower` | Convierte una letra mayúscula en minúscula. |
| `toupper` | Convierte una letra minúscula en mayúscula. |