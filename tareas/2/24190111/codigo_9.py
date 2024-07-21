def verificar(n):
    cnt = 0
    for b in range(1, n + 1):
        if n % b == 0:
            cnt += 1
    return cnt == 2

def primo(n):
    encontrados= 0
    candidato= 0

    while encontrados < n:
        candidato += 1
        if verificar(candidato):
            encontrados += 1
    return candidato

def main():
    with open('9_entrada.txt','r') as entrada:
        a= int(entrada.readline())
    z= primo(a)
    with open('9_salida.txt', 'w') as salida:
        salida.write("El "+ str(a) +"-ésimo número primo es: " + str(z))

if __name__ =="__main__":
    main()
