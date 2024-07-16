def aproximar_e(n):
    base = 1.0 + 1.0 / n
    e = 1.0
    for _ in range(n):
        e *= base
    return e
inicio = int(input("Ingrese el valor inicial de n: "))
fin = int(input("Ingrese el valor final de n: "))
for n in range(inicio, fin + 1):
    e = aproximar_e(n)
    #precisamos solo 15 decimalessss
    print(f"n = {n} e = {e:.15f}")