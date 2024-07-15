# Expresión balanceada

Escriba un programa que valida
si una expresión compuesta por
paréntesis, corchetes y llaves
en una cadena está balanceada.
Como ejemplo de cadena balanceada, considere

```cpp
{ s = 2 * (a[2] + 3); x = (1 + (2)); }
```

Si recorres la cadena cuidadosamente,
descubrirás que todos los
paréntesis, corchetes y llaves
están correctamente anidados y
cada una de las aperturas está emparajada con una cerradura.

Por otro lado, ejemplos de cadenas desbalanceadas son los siguientes:

- `(([])` pues falta cerrar un paréntesis.
- `)(` pues existe una cerradura de paréntesis antes de una apertura.
- `{(})` pues los signos están incorrectamente anidados.