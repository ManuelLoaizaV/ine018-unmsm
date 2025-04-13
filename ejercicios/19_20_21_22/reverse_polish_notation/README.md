# Reverse Polish Notation

Una de las aplicaciones más notorias de pilas
es en las calculadoras electrónicas,
las cuales son utilizadas para almacenar resultados intermedios.
El rol de las pilas en las calculadoras es más fácil de observar
en las primeras calculadoras científicas que
requerían al usuario ingresar las expresiones en
**Reverse Polish Notation** (RPN).

Por ejemplo, para computar el resultado de la expresión
`8.5 * 4.4 + 6.9 / 1.5`
en una calculadora RPN debemos ingresar
`8.5 ENTER 4.4 * 6.9 ENTER 1.5 / +`.

Cuando el botón `ENTER` es presionado, la calculadora toma
el valor anterior y lo añade a la pila.
Cuando el botón de algún operador es presionado,
la calculadora primero valida que el usuario haya ingresado algún valor.
De ser así, añade automáticamente este elemento a la pila y
computa el resultado aplicando el operador de la siguiente manera:

- Extrae los dos últimos valores en el tope de la pila.
- Aplica la operación aritmética especificada por el botón a estos valores.
- Apila el resultado en la pila.

Implementar una calculadora RPN en C++
requiere realizar ciertos cambios en la interfaz del usuario.
En una calculadora real, los dígitos y las operaciones
aparecen en el teclado.
En nuestra implementación, es más fácil imaginarse
que el usuario ingresa líneas en la consola,
cada línea tomando una de las siguientes formas:

- Un número de punto flotante.
- Un operador aritmético escogido del conjunto `+`, `-`, `*` y `/`.
- La letra `Q` que termina el programa.
- La letra `H` que imprime una ayuda.
- La letra `C` que vacía la pila.

Como el usuario ingresará cada número en una línea separada,
no habrá necesidad de definir una contraparte para el botón `ENTER` de la calculadora.
