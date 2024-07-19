from collections import deque

def imprimir_pila(pila):
    print()
    while pila:
        print (pila.pop())
    print()
    
def invertir_cola(cola):
    pila= []
    while cola:
        pila.append(cola.popleft())
    while pila:
        cola.appendleft(pila.pop())

def Roll(pila,n,k):
    print(f"Roll {n} {k} ")

    ultimos = deque()

    for i in range(n):
        ultimos.appendleft(pila.pop())

    offset = k % n

    for i in range(offset):
        ultimos.append(ultimos.popleft())

    invertir_cola(ultimos)

    while ultimos:
        pila.append(ultimos.popleft())

pila = deque(['D','C','B','A'])
#por alguna razon el codigo solo me da hasta la primera imprime_pila, pero despues de eso funciona bien
imprimir_pila(pila)

Roll(pila, 4, 1)
imprimir_pila(pila)

Roll(pila, 3, 2)
imprimir_pila(pila)

Roll(pila, 3, 2)
imprimir_pila(pila)

Roll(pila, 2, 4)
imprimir_pila(pila)








        


              