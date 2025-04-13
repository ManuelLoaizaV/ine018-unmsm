# Intersección de círculos

```cpp
bool IntersectanCirculos(
    double x1, double y1, double r1,
    double x2, double y2, double r2
)
```

Un círculo está caracterizado por su centro
$(x, y)$ y su radio $r > 0$.

Escriba una función que reciba las características
de dos círculos y retorne `true`
si es que se intersectan en al menos un punto.
En caso contrario, retorne `false`.

Para resolver este problema,
defina otra función que le permita
calcular la distancia entre dos puntos:

```cpp
double Distancia(double x1, double y1, double x2, double y2)
```