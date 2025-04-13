# Área entre las rectas

```cpp
double CalcularAreaEntreLasRectas(double m1, double b1, double m2, double b2, double m3, double b3)
```

Escriba una función que recibe seis números reales representando tres rectas:

$$y = m_1 x + b_1,$$

$$y = m_2 x + b_2,$$

$$y = m_3 x + b_3.$$

Primero encuentre en donde se intersecta cada par de rectas.
Luego retorne el área del triángulo formado
al conectar estos tres puntos de intersección.
Si dicho triángulo no existe (i.e. algún par de rectas es paralela),
retorne 0.

Para resolver el problema, defina tres funciones:
la primera para encontrar dónde se intersectan dos rectas (invocar esta función tres veces),
la segunda para calcular la distancia entre dos puntos,
la tercera para calcular el área del triángulo dadas las longitudes de sus lados.
Puede que te interese leer sobre [la fórmula de Herón](https://mathworld.wolfram.com/HeronsFormula.html).
