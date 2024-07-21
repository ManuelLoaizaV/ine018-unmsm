with open('Conjetura_de_Collatz_entrada.txt', 'r') as entrada:
    n = int(entrada.readline())

pasos = 0
original = n

# En lugar de llaves, son dos puntos (:), donde el espaciado horizontal sí puede alterar lo que tratas de hacer.
# Los paréntesis en las condiciones tampoco son necesarios.

with open('Conjetura_de_Collatz_salida.txt', 'w') as salida:
    while n > 1:
        if n % 2 == 0:
            m = n / 2
            mensaje = str(n) + " es par, entonces tomo la mitad: " + str(m) + "\n"
        else: 
            m = 3 * n + 1
            mensaje = str(n) + " es impar, entonces hago 3n + 1: " + str(m) + "\n"
        
        salida.write(mensaje)

        n = m
        pasos += 1

    mensaje_final = (
        "Wow, fue un viaje de " + str(pasos) + " paso(s) desde " + str(original) + " hasta 1." + "\n" +
        "Pero al final llegué. Eso quiere decir que " + str(original) + " es maravilloso." + "\n" +
        "Me pregunto qué números no serán maravillosos..."
    )
    salida.write(mensaje_final)

# Por lo demás, me agrada que los operadores sean similares a C++.

