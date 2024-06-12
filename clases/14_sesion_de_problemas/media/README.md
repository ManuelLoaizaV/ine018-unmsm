# Media

En estadística, una colección de datos es usualmente referida como **distribución**.
Uno de los principales objetivos del análisis estadístico
es encontrar maneras de comprimir un conjunto de datos
en estadísticas que expresen propiedades de la distribución como un todo.
La medida estadística más común es la **media**,
la cual es el promedio tradicional.
Para la distribución,
$x_1, x_2, \dots, x_n$,
la media suele ser representada como
$$
\overline{x} = \frac{\sum_{i=1}^n x_i}{n}.
$$.
Escriba una función
```cpp
long double Media(vector<long double>& datos)
```
que retorne la media del vector de datos.