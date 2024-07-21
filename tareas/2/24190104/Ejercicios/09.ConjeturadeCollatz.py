n = 27
pasos = 0

original = n

while n > 1:
    if n % 2 == 0:
        # Si n es par, lo dividimos por 2
        m = n // 2
    else:
        # Si n es impar, calculamos 3n + 1
        m = 3 * n + 1
    # volvemos n a m
    n = m
    # sumamos al contador
    pasos += 1

print(pasos)





