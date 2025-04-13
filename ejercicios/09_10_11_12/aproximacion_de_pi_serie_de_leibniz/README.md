# Aproximación de $\pi$ - Serie de Leibniz

El matemático alemán Leibniz (1646-1716)
descubrió que la constante matemática $\pi$
puede ser computada utilizando la siguiente serie:

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \dots = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k + 1}$$

Si comienzas con 1,
le quitas un tercio,
le sumas un quinto,
y así sucesivamente,
para cada número impar,
obtienes un número cada vez más cercano a $\pi/4$.

Escribe un programa que calcule una aproximación de $\pi$
dada por los 10000 primeros términos de [la serie de Leibniz](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80).