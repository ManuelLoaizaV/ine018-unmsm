# Superposición de rectángulos

```cpp
bool SuperponenRectangulos(
    int x1, int y1, int alto_1, int ancho_1,
    int x2, int y2, int alto_2, int ancho_2
)
```

Sea $(x, y)$ las coordenadas de la esquina superior izquierda
de un rectángulo con alto $h$ y ancho $w$.
Luego, las cuatro esquinas del rectángulo son las siguientes:
$(x, y), (x, y + h), (x + w, y)$ y $(x + w, y + h)$.

Dada las características de dos rectángulos,
escriba una función que retorne
`true` si es que los rectángulos
tienen al menos un punto en común,
`false` en caso contrario.
