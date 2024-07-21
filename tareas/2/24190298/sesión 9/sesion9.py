def EsNumeroPrimo(n):
    contador=0
    for x in range(1,n+1):
        if n % x == 0:
            contador=contador+1
    return contador ==2

def IesimoPrimo(i):
    primos=0
    posible=0

    while primos< i:
        posible=posible+1
        if EsNumeroPrimo(posible):
            primos=primos+1
    return posible

if __name__ == "__main__":
    n=input("Ingrese el n-ésimo primo que desea: ")
    n=int(n)
    print(IesimoPrimo(n))