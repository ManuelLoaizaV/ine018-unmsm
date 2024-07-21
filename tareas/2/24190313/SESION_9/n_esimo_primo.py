def es_primo(n):
    contador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador = contador + 1
    return contador == 2
def i_esimo_primo(i):
    primos_encontrados = 0
    candidato = 0
    while primos_encontrados < i:
        candidato = candidato + 1
        if es_primo(candidato):
            primos_encontrados = primos_encontrados + 1
    return candidato
i = int(input("Ingrese el valor de <<i>>: "))
print(f"El {i}-ésimo primo es: {i_esimo_primo(i)}")