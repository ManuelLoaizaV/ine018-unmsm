# Histograma
Un **histograma** es una manera gráfica de mostrar los datos
dividiendo los datos en rangos separados y luego indicando
cuántos valores caen en cada rango.
Por ejemplo, dadas las notas del examen
$$20, 19, 9, 17, 17, 18, 15, 17, 16, 14, 11, 16$$
un histograma tradicional tiene la siguiente forma:

![Histograma de notas](/assets/images/scores_histogram.jpeg)

Cuando generes histogramas usando la computadora,
es mucho más simple mostrarlos verticalmente de la siguiente manera:

```
00:
02:
04:
06:
08: *
10: *
12:
14: **
16: ****
18: **
20: *
```

Escriba un programa que reciba un vector de enteros
y muestre un histograma con esas notas,
dividido en los rangos [0, 2), [2, 4), [4, 6), y así sucesivamente
hasta el rango que contiene únicamente al valor 20.
Tu programa debe generar una salida que se parezca al ejemplo en cuanto sea posible.