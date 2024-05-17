# Funciones

El concepto de función es muy cercano al que conocemos en matemáticas,
solo que en C++ es un poco más general.

## Funciones en matemáticas

Toda función $f$ tiene dos conjuntos asociados a sí:
su **dominio** y su **rango**.

Una función $f$ solo puede ser aplicada
a elementos de su dominio.
Para todo $x$ en el dominio,
$f(x)$ pertenece al rango.

Si una función $f$ tiene como dominio $A$
y rango $B$, escribimos $f: A \to B$.

Formalmente, las siguientes reglas deben cumplirse:
- Primero, toda entrada en $A$ mapea a una salida en $B$.
Es decir, para todo $a \in A$ existe $b \in B$ tal que $f(a) = b$.
- Segundo, $f$ debe ser determinística: toda entrada produce la misma salida.
Es decir, para todo $a_1$ y $a_2$ en $A$, si $a_1 = a_2$ entonces $f(a_1) = f(a_2)$.

Por ejemplo, definamos la función valor absoluto $|\cdot|: \mathbb{R} \to \mathbb{R}$ con
$$
|x| = \begin{cases}
x & \text{si } x \geq 0,\\
-x & \text{si } x < 0.
\end{cases}
$$

> [!NOTE]
> La función debe estar definida
> para todo el elemento en el dominio.

> [!NOTE]
> La salida de la función
> siempre debe estar en el rango,
> pero no todos los elementos del rango
> deben producirse como salida.

## Funciones en programación

En los lenguajes de programación,
el concepto de función es más general que en matemáticas.
Como en las matemáticas, las funciones en C++ puedes especificar valores de entrada;
sin embargo, no tienen por qué hacerlo.
Similarmente, las funciones en C++ no tienen por qué retornar un resultado.

Una **función** es un bloque de código que ha sido organizado
y separado en una unidad aparte a la cual se le ha dado un nombre.

El acto de utilizar el nombre de la función para invocar el código
es conocido como **llamar** una función.

Para especificar una llamada a una función en C++,
escribimos el nombre de la función seguido
de una lista de expresiones encerradas entre paréntesis.
Estas expresiones, llamadas **argumentos**,
permiten al programa enviar información a la función.

Una vez realizada la llamada,
la función utiliza los datos proporcionados como argumentos,
realizar su trabajo,
y regresa al programa en el punto en el cual
la llamada fue realizada.
A este proceso se llama **retornar** de una función.
Al retornar, es común que la función traiga consigo un valor para quien la llamó.
A esta operación la llamamos **retornar un valor**.

# Funciones en C++

En C++, la definición de una función tiene la siguiente forma:

```
tipo nombre(parámetros) {
    ...
}
```

En este ejemplo, `tipo` es el tipo retornado por la función,
`nombre` es el nombre de la función, y
`parámetros` es una lista de declaraciones separadas por comas,
especificando el tipo y el nombre de cada parámetro de la función.

Un `parámetro` representa uno de los argumentos provistos en la llamada a la función
y actúa como una variable local en la mayoría de casos,
la única diferencia es que cada parámetro es inicializado automáticamente
con el valor del argumento correspondiente.

El cuerpo de la función es un bloque conformado por sentencias que implementan la función.
Las funciones que retornan un valor a quienes las llamaron requieren al menos una sentencia `return`
de la siguiente forma:

```cpp
return expresión;
```

Ejecutar una sentencia `return` hace que
la función inmediatamente retorne el valor de la expresión como el valor de la función.

Por otro lado, todas las funciones no tienen por qué retornar un valor.
Estas funciones que no retornan un valor y son ejecutadas por los efectos de su ejecución
suelen ser llamadas **procedimientos**
Para indicar que una función es un procedimiento
utilizaremos la palabra reservada `void` en el tipo del resultado.
Un procedimiento suele terminar al alcanzar el final de las sentencias de su cuerpo,
pero para tempranamente terminar la ejecución de un procedimiento podemos ejecutar
la sentencia `return` sin ninguna expresión de la siguiente manera:

```cpp
return;
```

Por ejemplo, definamos la función valor absoluto en C++:

```cpp
double ValorAbsoluto(double x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```
