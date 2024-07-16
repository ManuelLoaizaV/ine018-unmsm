# Colas

En nuestra sociedad,
una noción colectiva de justicia
suele ser asignar cierta prioridad a ser primero.
En programación, a esta estrategia de orden se le llama
"first in, first out"
y es abreviada como **FIFO**.

Una estructura de datos que almacena elementos
usando el paradigma FIFO es llamada **cola**.

Las operaciones fundamentales en una cola son llamadas
**encolar** y **desencolar**.

La operación **encolar** añade un nuevo elemento al final
de la cola, el cual es tradicionalmente llamado **cola**.

La operación **desencolar** elimina un elemento al inicio
de la cola, el cual es tradicionalmente llamado **cabeza**.

![Cola](https://miro.medium.com/v2/resize:fit:720/1*DRW4lVeUoIc2qS6Wel4Caw.png)

Como debes esperar por el hecho de que los modelos son similares,
la estructura de la clase `queue` es casi la misma
que su contraparte `stack`.

| Método | Descripción |
|--------|-----------|
| `size()` | Retorna el número de elementos actualmente en la cola. |
| `empty()` | Retorna `true` si la cola está vacía. |
| `push(valor)` | Inserta `valor` en la cola de la cola. |
| `pop()` | Elimina un elemento de la cabeza de la cola. |
| `front()` | Retorna el valor en la cabeza de la cola sin eliminarlo. |
