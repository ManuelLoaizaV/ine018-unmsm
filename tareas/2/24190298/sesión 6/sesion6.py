import math
def EsCuadradoPerfecto(N):
    N=int(N) 
    if N<0:
        return False
    raíz= int(math.sqrt(N))
    return raíz*raíz==N

if __name__ == "__main__":
    N= input("Ingrese el número: ")
    print(EsCuadradoPerfecto(N))