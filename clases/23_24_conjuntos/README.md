# Conjuntos

Una de las colecciones más útiles es la clase `set`
Esta clase modela la abstracción matemática de un **conjunto**,
el cual es una colección de elementos sin un orden
en el cual cada valor aparece una sola vez.

## Interfaz `set`

| Constructor | Descripción |
| ----------- | ----------- |
| `set<tipo>()` | Crea un set vacío conteniendo valores del tipo especificado. |

| Método | Descripción |
| ------ | ----------- |
| `size()` | Retorna el número de elementos en el conjunto. |
| `empty()` | Retorna `true` si el conjunto está vacío. |
| `insert(valor)` | Inserta el valor en el conjunto. |
| `erase(valor)` | Eliminar *valor* del conjunto. |
| `contains(valor)` | Retorna `true` si el valor pertenece al conjunto. |
| `clear()` | Eliminar todos los elementos del conjunto. |

## Iterando sobre una colección

Iterar sobre los elementos de una colección es una operación fundamental.
Si las bibliotecas están bien diseñadas,
los usuarios deberían poder utilizar la misma estrategia para realizar esta operación,
independiente de tratarse de una cadena, vector, set o map.
STL nos provee un mecanismo para realizar esto llamado **iterador**.
Un prerrequisito para poder entender iteradores
es tener familiaridad con detalles a bajo nivel de C++ como los punteros.

Desde C++11 tenemos un nuevo patrón de control llamado
**bucle for basado en rangos** con la siguiente forma:

```cpp
for (tipo variable : colección) {
    cuerpo del bucle
}
```

Por ejemplo, dada la cadena `username`

```cpp
string username = "Manuel123Loaiza456";
```

Si queremos contar el número de dígitos, tradicionalmente implementaríamos lo siguiente:

```cpp
int cnt = 0;
for (int i = 0; i < username.size(); i++) {
    if (isdigit(username[i])) {
        cnt++;
    }
}
```

Equivalentemente, podemos utilizar nuestra nueva estructura:

```cpp
int cnt = 0;
for (char c : username) {
    if (isdigit(c)) {
        cnt++;
    }
}
```

Cuando uno utiliza el bucle for basado en rangos,
a veces sirve saber en qué orden son procesados los elementos. No existe una regla universal.
Cada colección define su orden de iteración,
usualmente considerando la eficiencia.
- Cuando iteras a través de elementos de la clase `vector`,
los elementos se obtienen en el orden de los índices; es decir,
primero el elemento cuya posición tiene el índice 0,
luego el que se encuentra en la posición con índice 1, y así sucesivamente hasta el final del vector.
- Cuando iteras a través de elementos de la clase `map`,
el bucle retorna las parejas llave/valor en el orden natural del tipo de las llaves.
- Cuando iteras a través de elementos de la clase `set`,
el bucle retorna los elementos en el orden natural del tipo de estos elementos.
- Uno no puede utilizar el bucle for basado en rangos con instancias de las clases `stack` y `queue`.
Permitir el acceso sin restricciones a estas estructuras viola el principio de
que solo un elemento es visible en un instante particular de tiempo.