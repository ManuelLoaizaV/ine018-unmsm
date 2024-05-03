# Paradero más cercano

```cpp
int ObtenerParaderoMasCercano(int calle)
```

Escriba una función que reciba un entero no negativo
representando la calle en la que te encuentras
y retorne la calle del paradero más cercano para que tomes el bus.
Existe un paradero cada 8 calles, incluyendo la calle 0.
En caso de empates, ir al paradero con la calle de menor número
(en los primeros paraderos el bus suele tener menos pasajeros).

```cpp
ObtenerParaderoMasCercano(19)  // 16
ObtenerParaderoMasCercano(24)  // 24
ObtenerParaderoMasCercano(28)  // 24
ObtenerParaderoMasCercano(29)  // 32
```