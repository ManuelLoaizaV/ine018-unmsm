# Vectores

Una de las colecciones más valiosas es la clase `vector`,
la cual nos provee una funcionalidad muy similar a la de los arreglos.
Los arreglos existen desde el nacimiento de la programación.
Como la mayoría de lenguajes de programación,
C++ provee arreglos. Sin embargo,
los arreglos tienen muchas debilidades:
- Debemos alocar arreglos con un tamaño fijo el cual no podemos modificar más adelante.
- A pesar de que los arreglos tengan tamaño fijo,
C++ no hace disponible el valor de este tamaño al programador.
Así, uno necesita una variable extra para poder contabilizar la cantidad de elementos.
- Tradicionalmente los arreglos no permiten insertar ni eliminar elementos.
- C++ no nos asegura que los elementos que tu accedas existan en el arreglo.
Por ejemplo, si creamos un arreglo de tamaño 25 y tratas de acceder al valor en la posición 50,
C++ simplemente accederá a la dirección de memoria en la cual dicho elemento con posición 50 aparecería si existiese.

La clase `vector` resuelve estos problemas reimplementando
el concepto de arreglo dinámico como un **Abstract Data Type** (ADT).

Como cliente de la clase `vector`, no estás interesado en la estructura interna
y puedes dejar esta labor a los programadores que implementan este ADT.
Usted está preocupado por otro tipo de cuestiones y desea respuestas a las siguientes preguntas:
1. ¿Cómo puedo especificar el tipo de objeto contenido en un `vector`?
2. ¿Cómo creo un objeto que es instancia de la clase `vector`?
3. ¿Qué métodos existen en la clase `vector` que implementan su comportamiento abstracto?

## Especificando el tipo base de un vector

En C++, el tipo de objetos que contendrá una colección se tiene que especificar
incluyendo el nombre del tipo entre cocodrilos luego del nombre de la clase.
Por ejemplo, la clase `vector<int>` representa un vector cuyo elementos son enteros,
`vector<char>` especifica un vector cuyos elementos son caracteres,
y `vector<string>` especifica un vector en el cual los elementos son cadenas.
El tipo encerrado entre cocodrilos es llamado el **tipo base** de la colección.

Las clases que requieren una especificación del tipo base se llaman **clases parametrizadas**.
En C++, estas clases parametrizadas son llamadas **templates**.
Debido a esto, el compilador trata a `vector<int>` y `vector<char>`
como clases independientes que comparten una estructura común.
El nombre `vector` actúa como una plantilla para una familia de clases en donde
la única diferencia es el tipo de valor que el vector contiene.
Por ahora solo debes entender cómo usar estas plantillas
y no cómo implementarlas.

## Declarando un objeto vector
Parte de la filosofía detrás de las estructuras de datos
es que el cliente piense estas como si fuesen tipos primitivos.
Luego, así como uno declara una variable entera tipeando
```cpp
int n;
```
uno declara un nuevo vector tipeando
```cpp
vector<int> v;
```

## Operaciones de vectores
Cuando declaras una variable del tipo `vector`,
esta comienza como un vector vacío,
lo cual significa que no contiene elementos.
Como un vector vacío no es particularmente útil,
una de las primeras cosas que debemos aprender es
cómo añadir un nuevo elemento a un objeto del tipo `vector`.
La manera usual de realizar esto es llamar al método `push_back`,
el cual añade un nuevo elemento al final del `vector`.
Por ejemplo, si `v` es un vector vacío de enteros y ejecutamos

```cpp
v.push_back(100);
v.push_back(6);
v.push_back(88);
v.push_back(9);
v.push_back(1);
v.push_back(59);
```

convertiremos a `v` en un vector conteniendo seis elementos.
Al igual que con los caracteres en una cadena,
C++ enumera los elementos de un vector comenzando desde cero:

![Métodos de un vector](https://assets.leetcode.com/users/images/d1bf940c-26e3-4db5-a582-b99b80600a79_1694697229.2238786.png)

### Acceder a elementos en un vector
Una de las características de C++ que lo distingue de otros lenguajes es que
las clases pueden sobrescribir la definición de los operadores estándares.
Esta funcionalidad hace posible que la clase `vector` soporte la sintaxis tradicional
y que podamos usar corchetes para especificar un índice deseado.
Así, para seleccionar el elemento en la posición $i$
podemos utilizar la expresión $v[i]$ tal y como con los arreglos.
Es más, podemos cambiar el valor de dicho elemento asignándole un nuevo valor.
Por ejemplo, si queremos asignarle $70$ al tercer elemento de $v$ escribiríamos
```cpp
v[2] = 70;
```

### Crear un vector de tamaño predefinido
Los ejemplos que hemos visto hasta ahora comienzan con un vector vacío
y luego le añadimos elementos, uno tras otro.
En muchas aplicaciones, construir un vector elemento por elemento puede ser tedioso,
especialmente si sabes el tamaño del vector con anticipación.
En esos casos, tiene sentido especificar el número de elementos como parte de la declaración.

Por ejemplo, supongamos que queremos un vector para almacenar
las notas redondeadas de los $60$ alumnos del curso.
La estrategia que ya conocemos es crear un vector vacío `vector<int>`
y luego añadirle $60$ elementos con un bucle `for` de la siguiente manera: 

```cpp
const int NUMERO_ALUMNOS = 60;
vector<int> notas;
for (int i = 0; i < NUMERO_ALUMNOS; i++) {
    notas.push_back(0.0);
}
```

Una manera más limpia sería incluir el tamaño como argumento de la declaración:

```cpp
vector<int> notas(NUMERO_ALUMNOS);
```

Esta declaración crea un `vector<int>` con `NUMERO_ALUMNOS` elementos, cada uno inicializado con $0$.
El resultado de los dos fragmentos de código es el mismo.
Ambos crear un `vector<int>` con $60$ ceros.
El primer código requiere que el programador inicialice los elementos;
el segundo cede esa responsabilidad a la clase `vector`.

### Interfaz `vector`

| Constructor | Descripción |
| ---- | ---- |
| `vector<tipo>()` | Crea un vector vacío. |
| `vector<tipo>(n, valor)` | Crea un vector con $n$ elementos, cada uno inicializado con $valor$, o de ser omitido, el valor por defecto de $tipo$. |

| Método | Descripción |
| ---- | ---- |
| `size()` | Retorna el número de elementos en el vector. |
| `empty()` | Retorna `true` si el vector está vacío. |
| `at(i)`| Retorna el elemento en la posición $i$. |
| `push_back(valor)` | Añade un nuevo elemento al final del vector. |
| `insert(it, valor)` | Inserta $valor$ antes de la posición especificada por el iterador. |
| `erase(it)` | Elimina el elemento de la posición especificada por el iterador. |
| `clear()` | Elimina todos los elementos del vector. |

| Operador | Descripción |
| ---- | ---- |
| `v[i]` | Selecciona el elemento en la posición $i$. |
| `v = u` | Asigna el vector $u$ al vector $v$. |
| `v == u` | Retorna `true` si el contenido de $v$ y $u$ son iguales. Es decir, si $v.size()$ es igual a $u.size()$ y $v[i]$ es igual a $u[i]$ para $0 \leq i < v.size()$. |

## Representando estructuras de dos dimensiones

El tipo de parámetro utilizado en la clase `vector` puede ser cualquier tipo de C++, incluso sí mismo.
En particular, para crear una matriz podemos declarar un `vector` cuyo tipo base es también un `vector`.
La declaración
```cpp
vector<vector<int>> sudoku(9, vector<int>(9));
```
inicializa una variable `sudoku` como un `vector` de nueve elementos,
cada uno siendo un `vector` de nueve elementos.
El tipo base del vector interno es `int`,
y el tipo base del vector externo es `vector<int>`.
El tipo de toda la matriz es `vector<vector<int>>`.