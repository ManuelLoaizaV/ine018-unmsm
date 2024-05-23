# Cadenas

En esta clase introduciremos la biblioteca `<string>` de C++.

Asimismo, nos iremos familirizando con la noción de una **clase**,
término que utilizamos para tipos de datos afines al paradigma de programación orientada a objetos.
La mayoría de aplicaciones en C++ trabajan con objetos
de una clase llamada `string` para poder procesar texto.

Conceptualmente, una cadena es simplemente una sucesión de caracteres.
Por ejemplo, la cadena `"hola, mundo"` es una sucesión de once caracteres
conformada por nueve letras, una coma y un espacio.

En la [clase 3](/clases/03_tipos_variables_operadores_expresiones/)
aprendimos que los tipos de datos están definidos por un dominio y un conjunto de operaciones.
Para las cadenas, el dominio es el conjunto de todas las sucesiones de caracteres

Cuando declaramos una cadena,
solemos especificar el valor inicial como un literal de cadena,
la cual es una sucesión de caracteres entre comillas inglesas.
Por ejemplo, la siguiente declaración

```cpp
const string ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
```

asigna a la constante `ALFABETO` una cadena de 26 caracteres conteniendo letras mayúsculas.

Podemos utilizar los operadores `>>` y `<<` para leer y escribir valores a las cadenas.
Recuerde que el operador `>>` se detiene ni bien encuentra el primer
**whitespace**, el cual es definido como cualquier caracter visualizado como un espacio en blanco
cuando es mostrado en pantalla. Los caracteres whitespace más comunes son
el espacio y el salto de línea.

```cpp
int main() {
    string nombre;
    cout << "Ingrese su nombre: ";
    cin >> nombre;
    cout << "Hola, " << nombre << endl;
    return 0;
}
```

## Operaciones

Para realizar operaciones más complejas
usando la biblioteca `<string>`,
descubriremos que el tipo de dato `string`
no se comporta de la misma manera que
los tipos de datos más tradicionales.
Una de las principales diferencias yace
en la sintaxis para involcar funciones.

Por ejemplo,
si la biblioteca `<string>`
exporta una función llamada `length`,
imaginaríamos que para obtener el tamaño
de una cadena llamada `s`

```cpp
int longitud = length(s);
```

El problema con esta expresión es que
el tipo de datos `string` no es un tipo tradicional
sino una **clase**,
que informalmente lo podríamos definir
como una plantilla que describe
un conjunto de valores agrupados
con un conjunto de operaciones.
En la programación orientada a objetos,
las instancias de una clase son llamadas **objetos**.
Las operaciones
que aplican a las instancias de una clase
se llaman **métodos**.

En C++, un método se ve y comporta similar a una función
a diferencia de que está acoplado a la clase que pertenece.
Podríamos decir que las funciones tradicionales que conocemos
son **funciones libres** ya que no están atadas a una clase específica.

Así, la versión orientada a objetos del código anterior se vería de la siguiente manera:

```cpp
int longitud = s.length();
```

Aquí tenemos algunos operadores cotidianos:

| Operadores  | Descripción |
| ------------- | ------------- |
| `s + t`  | Concatena `s` y `t` uno luego del otro y retorna una nueva cadena conteniendo los caracteres combinados. |
| `s += t`  | Yuxtapone una copia de `t` al final de `s`. C++ sobrecarga este operador de tal manera que `t` también puede ser un caracter.  |
| `s == t` <br> `s != t` <br> `s < t` <br> `s <= t` <br> `s > t` <br> `s >= t` | C++ sobrecarga los operadores de comparación de tal manera que las cadenas se comparen utilizando el **orden lexicográfico**. |
| `s[i]` |  Retorna el caracter en la i-ésima posición de la cadena `s` como un valor asignable. |

Los siguientes métodos no modifican la cadena original:

| Operadores  | Descripción |
| ------------- | ------------- |
| `s.length()`  | Retorna el número de caracteres en la cadena `s`. |
| `s.substr(pos, n)` | Retorna una nueva cadena formada por a lo más `n` caracteres iniciando desde la posición `pos`. |
| `s.compare(t)` | Compara la cadena `s` con la cadena `t` lexicográficamente y retorna un entero que puede ser `0` si las cadenas son iguales, negativo si `s` precede `t` y positivo si `t` precede a `s`. |

Los siguientes métodos modifican la cadena original:

| Operadores  | Descripción |
| ------------- | ------------- |
| `s.erase(pos, n)`  | Elimina `n` caracteres de `s` comenzando en `pos`. |
| `s.insert(pos, t)`  | Inserta una copia de `t` en `s` comenzando en `pos`. |
| `s.replace(pos, n, t)` | Reemplaza `n` caracteres de `s` comenzando en `pos` con una copia de la cadena `t`. |

