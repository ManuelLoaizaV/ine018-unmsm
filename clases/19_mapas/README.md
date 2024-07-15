# La clase `map`

En esta clase introduciremos otra colección genérica llamada `map`,
la cual es conceptualmente similar a un diccionario.
Un diccionario te permite buscar una palabra para leer su significado.
Un mapa es una generalización de esta identificación
entre una **llave** y su **valor** asociado.
En el ejemplo del diccionario,
la llave es la palabra que estamos buscando,
y el valor es su definición.
Un compilador para un lenguaje de programación utiliza una estructura de datos llamada
**tabla de símbolos** para asociar el nombre de una variable con su valor correspondiente,
el cual es otro nombre para el mismo concepto.

## La estructura de la clase `map`

Al igual que las colecciones que hemos estudiado hasta ahora,
`map` es un template parametrizado por el tipo de la llave y el tipo del valor.
Por ejemplo, si queremos simular un diccionario en el cual a cada palabra
le asociamos su definición, declaramos lo siguiente:

```cpp
map<string, string> diccionario;
```

Análogamente, si estás implementando un lenguaje de programación,
puedes usar un `map` para guardar los valores de variables de punto flotante
asociando sus nombres a sus valores de la siguiente manera:

```cpp
map<string, double> tabla_de_simbolos;
```

Estas definiciones crean mapas vacíos que no contienen llavores ni valores.
En cualquiera de los casos, posteriormente tenemos que añadir parejas llave/valor al mapa.

![Diccionario en Python](https://miro.medium.com/v2/resize:fit:946/1*5fEx6NdjGTrVBy70LKA7aQ.png)

## Interfaz `map`
| Constructor | Descripción |
| ------ | ----------- |
| `map<tipo de llave, tipo de valor>()` | Crea un mapa vacío asociando llaves y valores. |

| Método | Descripción |
| ------ | ----------- |
| `size()` | Retorna el número de parejas llave/valor en el mapa. |
| `empty()` | Retorna `true` si el mapa está vacío. |
| `insert({llave, valor})` | Asocia *llave* y *valor* en el mapa. Si *llave* no ha sido definida previamente, una nueva entrada es añadida. Si una asociación anterior existe, el valor anterior es reemplazado por el nuevo. |
| `at(llave)` | Retorna el valor asociado con *llave* en el mapa. |
| `erase(llave)` | Elimina *llave* del mapa junto con su valor asociado. |
| `contains(llave)` | Verifica si *llave* está asociada con algún valor. De ser cierto, retorna `true`. |
| `clear()` | Elimina todas las parejas llave/valor del mapa. |

| Operador | Descripción |
| -------- | ----------- |
| `m[llave]` | La clase `map` sobrecarga el operador `[]` haciendo que un mapa actúe como un arreglo asociativo indexado por una llave. Si la llave no existe en el mapa, una nueva entrada con el valor por defecto del tipo es creada. |

## Mapas como arreglos asociativos

La clase `map` sobrecarga el operador `[]` usado para seleccionar elementos de arreglos
de tal manera que la sentencia

```cpp
m[llave] = valor;
```

equivale a

```cpp
m.insert({llave, valor});
```

Asimismo, la expresión `m[llave]` retorna el valor de `m` asociado con `llave`
exactamente como lo hace `m.at(llave)`.

Esta notación es bastante conveniente porque no tenemos que memorizar muchas funciones,
pero también curiosa puesto que los arreglos y los mapas tienen estructuras muy diferentes.

Usar la sintaxis de arreglos para realizar operaciones de mapas
se ha vuelto bastante popular en lenguajes de programación contemporáneos.
Muchos lenguajes implementan sus arreglos internamente como mapas,
haciendo posible indexar valores que no necesariamente son enteros.
A este ADT se le llama **arreglo asociativo**.