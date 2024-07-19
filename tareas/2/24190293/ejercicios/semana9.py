i = int(input("Ingrese el valor de i para encontrar el i-ésimo primo: "))
primos_encontrados = 0
candidato = 0

while primos_encontrados < i:
    candidato = candidato + 1
    cantidad_divisores = 0
    for j in range(1, candidato + 1):
        if candidato % j == 0:
            cantidad_divisores = cantidad_divisores + 1
    if cantidad_divisores == 2:
        primos_encontrados = primos_encontrados + 1

print(candidato)