# Conjetura de Collatz

[Gödel, Escher, Bach: an Eternal Golden Braid](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach),
libro ganador del Premio Pulitzer escrito por [Douglas Hofstadter](https://en.wikipedia.org/wiki/Douglas_Hofstadter),
contiene muchos acertijos matemáticos
de los cuales algunos se prestan a ser programados.

En el capítulo XII, Hofstadter menciona un problema bello
que calza perfecto con nuestra séptima clase.
Aquí un fragmento de la conversación entre la tortuga y Aquiles de la página 401:


> Aquiles: ¿Qué tal 15?
>
> Tortuga: Es una buena elección. Empezamos por tu número, y si es impar,
> lo triplicamos y añadimos 1.
> Si es par, tomamos la mitad.
> Luego repetimos este proceso.
> Llamemos a tu número maravilloso si eventualmente alcanza ser 1.
>
> Aquiles: ¿Será 15 maravilloso? Veamos:
```
15 es impar, entonces hago 3n + 1: 46
46 es par, entonces tomo la mitad: 23
23 es impar, entonces hago 3n + 1: 70
70 es par, entonces tomo la mitad: 35
35 es impar, entonces hago 3n + 1: 106
106 es par, entonces tomo la mitad: 53
53 es impar, entonces hago 3n + 1: 160
160 es par, entonces tomo la mitad: 80
80 es par, entonces tomo la mitad: 40
40 es par, entonces tomo la mitad: 20
20 es par, entonces tomo la mitad: 10
10 es par, entonces tomo la mitad: 5
5 es impar, entonces hago 3n + 1: 16
16 es par, entonces tomo la mitad: 8
8 es par, entonces tomo la mitad: 4
4 es par, entonces tomo la mitad: 2
2 es par, entonces tomo la mitad: 1
```
> ¡Guau! Fue un viaje bastante largo desde 15 hasta 1.
> Pero al final llegué. Eso quiere decir que 15 es maravilloso.
> Me pregunto qué números no serán maravillosos ...

Como puedes ver en el ejemplo, los números suben y bajan,
pero eventualmente, al menos para todos las sucesiones que se han computado comenzando con números menores a $2^{68}$,
siempre terminan en el número 1.
Cada una de estas sucesiones es conocida como [Hailstone sequence](https://mathworld.wolfram.com/HailstoneNumber.html).

Escriba un programa que reciba un número entero positivo e imprime su Hailstone sequence
como en el libro de Hofstadter, seguida de una línea mostrando el número de pasos que tomó para alcanzar 1.

> [!NOTE]
> Un dato interesante es que nadie ha podido probar de que este procedimiento siempre termina..
> A este problema se le conoce como [la conjetura de Collatz](https://mathworld.wolfram.com/CollatzProblem.html).
> El número de pasos a veces puede tornarse arbitrariamente grande. Por ejemplo, ¿cuántos pasos toma cuando $n$ es 27?