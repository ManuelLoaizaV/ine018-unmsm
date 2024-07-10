from collections import deque

def invertir_cola(cola):
    pila = []
    while cola:
        pila.append(cola.popleft())
    while pila:
        cola.append(pila.pop())

def roll(pila, n, k):
    ultimos = deque()
    for i in range(n):
        ultimos.append(pila.pop())
    # Creo que voy entendiendo el for con el range

    offset = k % n
    for i in range(offset):
        ultimos.append(ultimos.popleft())
    # Esto me copié de usted profe, su razonamiento jajaja

    invertir_cola(ultimos)

    while ultimos:
        pila.append(ultimos.popleft())

    return pila
# Ahora sí ^^

# Suponiendo que mis entradas son siempre válidas
# O sea:    NO n > tamaño, NO n < 0, NO k < 0

with open("Roll_entrada.txt", "r") as entrada:
    linea = entrada.readline().split()
    linea1 = entrada.readline().split()  
    linea2 = entrada.readline().split()
    linea3 = entrada.readline().split()

    pila_principal = []

    for chars in linea:
        pila_principal.append(chars)

    x1 = int(linea1[0])
    x2 = int(linea1[1])

    dx1 = int(linea2[0])
    dx2 = int(linea2[1])

    dwx1 = int(linea3[0])
    dwx2 = int(linea3[1])

resultado = roll(pila_principal.copy(), x1, x2)
resultado1 = roll(pila_principal.copy(), dx1, dx2)
resultado2 = roll(pila_principal.copy(), dwx1, dwx2)
# Literal es como si estuviera copiando la cadena, no la toco pues para
# los tres es la misma

with open("Roll_salida.txt", "w") as salida:
    salida.write("Resultado: " + " ".join(resultado) + "\n" +
                 "Resultado: " + " ".join(resultado1) + "\n" +
                 "Resultado: " + " ".join(resultado2))
    # El "".join() es para covertir mi lista en cadena y quitar los [ ]
    # y separar sus elementos por un " "