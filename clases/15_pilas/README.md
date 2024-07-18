# Pilas

La colección más simple en términos de operaciones provistas
es la clase `stack`.
Conceptualmente, una **pila** provee
almacenamiento para una colección de datos
sujeta a la restricción que los valores
deben ser eliminados de la pila en
el orden opuesto al cual fueron añadidos.
Esta restricción implica que el último elemento
añadido a la pila es siempre el primer elemento
en ser eliminado.

Este orden con el cual las pilas son procesadas
es llamado **LIFO**, el cual significa
"last in, first out".

![Pila de platos](https://qph.cf2.quoracdn.net/main-qimg-9016d7b4c553ccaa0f1eda9bb9ea84ef)

La razón principal por la que las pilas
son importantes en programación es que
las llamadas anidadas a las funciones
se comportan como una pila.
Por ejemplo, si la función `main`
llama a una función `f`,
un registro con información relacionada a `f`
es apilado encima del registro de la función `main`.
Si `f` llama a una función `g`,
un nuevo registro para `g` es apilado
encima del registro de `f`.
Cuando `g` retorna, su registro
es eliminado de la pila
retaurando `f` a la superficie de la pila.

## La estructura de la clase `stack`

Al igual que `vector`,
`stack` es una colección que requiere que
especifiques el tipo de elementos.
Por ejemplo, `stack<int>` representa una pila
cuyos elementos son enteros, y
`stack<string>` representa una pila de cadenas.
Similarmente, si uno define sus clases
`Plato` y `Registro`, uno puede crear una pila
con estos objetos usando las clases
`stack<Plato>` y `stack<Registro>`.

A continuación algunos métodos de la interfaz `stack`:

| Método | Descripción |
|--------|-----------|
| `size()` | Retorna el número de elementos actualmente en la pila. |
| `empty()` | Retorna `true` si la pila está vacía. |
| `push(valor)` | Inserta `valor` en la pila tal que este ser convierte en el tope. |
| `pop()` | Elimina el valor en el tope de la pila. |
| `top()` | Retorna el valor en el tope de la pila sin eliminarlo. |
