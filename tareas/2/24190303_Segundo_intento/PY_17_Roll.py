def imprimir_pila(pila):
    print()
    for elemento in reversed(pila):
        print(elemento)
    print()

def Roll(pila, n, k):
    elementos = []
    for _ in range(n):
        elementos.append(pila.pop())

    k = k % len(elementos)

    for _ in range(k):
        elementos.insert(0, elementos.pop())

    for _ in range(n):
        pila.append(elementos.pop())

pila = ['A', 'B', 'C', 'D']

imprimir_pila(pila)

Roll(pila, 4, 1)
imprimir_pila(pila)

Roll(pila, 3, 2)
imprimir_pila(pila)

Roll(pila, 2, 4)
imprimir_pila(pila)
