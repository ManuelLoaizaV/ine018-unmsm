def Roll(pila, n, k):
    if n < 0 or k < 0:
        print("roll: argument out of range")
        return
    
    if not pila or n >= len(pila):
        print("roll: argument out of range")
        return
    
    elementos = []
    for _ in range(n):
        elementos.append(pila.pop()) 
 # cuando y si es que k es mayor que n, para que pueda seguir haciendo la rotación   
    k = k % len(elementos) 
    
    for _ in range(k):
        elementos.insert(0, elementos.pop())
    
    for _ in range(n):
        pila.append(elementos.pop())

pila1 = ['A', 'E', 'I', 'O', 'U']

Roll(pila1, 5, 1)
print(pila1)

Roll(pila1, 3, 2)
print(pila1)

Roll(pila1, 6, 4)
print(pila1)
