# Fila del supermercado

![Compras en supermercado](https://peruretail.sfo3.cdn.digitaloceanspaces.com/wp-content/uploads/app-reducir-colas-centros-comerciales.jpg)

Implemente un programa que simule una fila de pago en el supermercado.
Los clientes llegan a la caja y se paran al final de la fila.
Estos clientes esperan en la fila hasta que la cajera esté disponible.
La cajera está ocupada por un periodo de tiempo atendiendo a un cliente en particular.
Tras completar su servicio, inmediatamente comenzará a atender al siguiente cliente en la fila.

En cada unidad de tiempo,
hasta la constante `TIEMPO_DE_SIMULACION`,
las siguientes operaciones son realizadas:
1. Determinar si un nuevo cliente llega a la fila.
Los nuevos clientes llegan aleatoriamente con una probabilidad
determinada por la constante `PROBABILIDAD_DE_LLEGADA`.
2. Si la cajera está ocupada, esta invertirá una unidad de tiempo adicional con su cliente.
Eventualmente, el tiempo para atender a su cliente terminará
y la cajera se liberará.
3. Si la cajera está libre,
atenderá al siguiente cliente en la fila en caso exista.
El tiempo de servicio es un periodo aleatorio entre
`TIEMPO_MINIMO_DE_SERVICIO` y `TIEMPO_MAXIMO_DE_SERVICIO`.

Al final de la simulación,
el programa mostrará las constantes de la simulación
y los siguientes resultados:
- El número de clientes atendidos.
- El tiempo promedio de espera en la fila.
- El número promedio de personas en la fila.
