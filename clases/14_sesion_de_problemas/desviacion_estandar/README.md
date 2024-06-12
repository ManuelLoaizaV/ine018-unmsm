# Desviación estándar
Otra medida estadística común es la **desviación estándar**,
la cual provee un indicador de qué tanto los valores en la
distribución $x_1, x_2, \dots, x_n$ difieren de la media.
Matemáticamente, la desviación estándar $\sigma$ es expresada como
$$
\sigma = \sqrt{\frac{\sum_{i=1}^n (\overline{x} - x_i)^2}{n}}.
$$
Escriba una función
```cpp
long double DesviacionEstandar(vector<long double>& datos)
```
que retorne la desviación estándar de la distribución de datos.