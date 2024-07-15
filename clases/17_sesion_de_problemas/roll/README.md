# roll

PostScript es un lenguaje de programación orientado a pilas
creado por Adobe Corporation en los ochentas.
Toda la data del programa es almacenada en una pila.
Muchos operaadores disponibles en PostScript
tienen el efecto de manipular la pila de alguna manera.
Por ejemplo, tenemos el operador `pop` que elimina el elemento en el tope de la pila,
o el operador `exch` que intercambia los dos elementos que se encuentren en el tope de la pila.

Uno de los operadores más interesantes de PostScript es el operador `roll`,
el cual toma dos argumentos: $n$ y $k$.
El efecto de aplicar `n k roll` es rotar los $n$ elementos del
tope de la pila $k$ posiciones cíclicamente.

Por ejemplos, supongamos que tenemos la pila `A B C D`.

Si le aplicamos `4 1 roll` obtenemos `D A B C`.

Si le aplicamos `3 2 roll` obtenemos `A C D B`. 

Si le aplicamos `2 4 roll` obtenemos `A B C D`.

Escriba una función

```cpp
void Roll(stack<char>& pila, int n, int k)
```

que implemente aplicar la operación `n k roll` de PostScript sobre la pila especificada.
Tu implementación debe validar que $n$ y $k$ sean no negativos
y que $n$ no sea mayor que el tamaño de la pila.
Si alguna de las condiciones es violada, mostrar el mensaje
`roll: argument out of range`.
Note que $k$ puede ser más grande que $n$,
en ese caso la operación `roll` continúa con más de un ciclo.
En el último ejemplo hemos rotado cuatro veces los últimos dos elementos
de la pila dejándola tal y como estaba originalmente.