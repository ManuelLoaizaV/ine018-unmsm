n = 27
pasos = 0

original = n

while n > 1:
    if n % 2 == 0:
        m = n // 2
    else:
        m = 3 * n + 1
    n = m
    pasos += 1

print(pasos)