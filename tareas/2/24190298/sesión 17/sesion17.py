from collections import deque
def ImprimirPila(pila):
    while pila:
        print(pila.pop())
    print()

def roll(pila, n, k):
    print(f"Roll {n} {k}")
    if n==0:
        print("Pila vacía")
        return
    else:
        vuelta= k%n
        pila_deque = deque(pila)
        pila_deque.rotate(vuelta)
        pila[:]= list(pila_deque)

if __name__=="__main__":
    pila=['A','B','C','D']
    ImprimirPila(pila)

    n = len(pila)
    k = 1
    roll(pila, n, k )
    ImprimirPila(pila)