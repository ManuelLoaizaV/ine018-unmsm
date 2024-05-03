# Ecuación de tercer grado

```cpp
void EncontrarRaicesEnterasDeCubica(double a, double b, double c, double d)
```

Escriba una función que reciba los coeficientes $a$, $b$, $c$ y $d$
de una ecuación cúbica de la siguiente forma:

$$
ax^3 + bx^2 + cx + d = 0.
$$

Está garantizado que la función tiene tres raíces reales y enteras.
Debes imprimir las tres raíces en orden creciente.

Para comenzar, querrás leer sobre la fórmula cúbica de Cardano [aquí](https://mathworld.wolfram.com/CubicFormula.html).
A partir de eso, puedes usar esta fórmula:
$$
x = \left(q + \left(q^2 + (r-p^2)^3\right)^{1/2}\right)^{1/3}
+ \left(q - \left(q^2 + (r-p^2)^3\right)^{1/2}\right)^{1/3}
+ p
$$
$$
p = -\frac{b}{3a}
$$
$$
q = p^3 + \frac{bc - 3ad}{6a^2}
$$
$$
r = \frac{c}{3a}
$$

Esto no es tan simple como parece
porque tu solución para $x$ no solo será aproximada
(y no exactamente un entero, así que tendrás que hacer algo al respecto),
sino que incluso puede que no sea real.
Aunque la solución es real,
los pasos intermedios pueden incluir algunos valores complejos,
y en estos casos la solución incluirá un valor imaginario (posiblemente pequeño).
Así que tendrás que convertir de complejo a real, y luego convertir de real a entero.

Genial, ahora tienes una raíz.
¿Qué pasa con las otras?
Bueno, podemos factorizar dicha raíz y eliminarla
quedándonos con una ecuación cuadrática,
que por supuesto es fácil de resolver.
Una explicación breve y clara de este paso la puedes encontrar en
[la sección de factorización](https://en.wikipedia.org/w/index.php?title=Cubic_function&oldid=917614036#Factorization)
en el artículo sobre funciones cúbicas en Wikipedia.
¡No olvides convertir estos en valores enteros!

Así que ahora tienes las tres raíces enteras.
¡Excelente trabajo!
Todo lo que queda es ordenarlas.
Ahora, si estuviésemos más adelantados en el curso,
podrías ponerlas en un vector y
llamar a una función que las ordene por ti.
Pero no es así, por lo que no puedes hacerlo.
En cambio,
averigua cómo ordenar estos valores usando las pocas funciones
disponibles en estas primeras clases.
Luego solo imprime estos tres valores y listo.