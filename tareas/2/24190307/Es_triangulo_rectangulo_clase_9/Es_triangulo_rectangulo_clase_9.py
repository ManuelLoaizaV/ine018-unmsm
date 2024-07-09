import math
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    raiz = math.sqrt(dx*dx + dy*dy)
    return raiz
# Ok, creo que era obvio lo de 'bibliotecas', pero me sorprendió verlo en Python

def triangulo_rectangulo(x1, y1, x2, y2, x3, y3):
    a = distancia(x1, y1, x2, y2)
    b = distancia(x1, y1, x3, y3)
    c = distancia(x2, y2, x3, y3)

    return a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
# Esto sí no lo esperaba, los condicionales se escriben, no son símbolos :o

with open('Es_Triangulo_rectangulo_entrada.txt', 'r') as entrada:
    posicion = entrada.readline().split()
    # Me sirvió esto profe, muchas gracias ^^
    x1 = int(posicion[0])
    y1 = int(posicion[1])
    x2 = int(posicion[2])
    y2 = int(posicion[3])
    x3 = int(posicion[4])
    y3 = int(posicion[5])

    posicion2 = entrada.readline().split()
    dx1 = int(posicion2[0])
    dy1 = int(posicion2[1])
    dx2 = int(posicion2[2])
    dy2 = int(posicion2[3])
    dx3 = int(posicion2[4])
    dy3 = int(posicion2[5])

Es_rectangulo = triangulo_rectangulo(x1, y1, x2, y2, x3, y3)
Es_rectangulo1 = triangulo_rectangulo(dx1, dy1, dx2, dy2, dx3, dy3)

if Es_rectangulo == True:
    valor = 1

if Es_rectangulo1 == True:
    valor1 = 1

if Es_rectangulo == False:
    valor = 0

if Es_rectangulo1 == False:
    valor1 = 0
# Esto lo hago para que se parezca a C++ xdxd

with open('Triangulo_rectangulo_salida.txt', 'w') as imprimo:
    imprimo.write(str(valor) + "\n" +
                  str(valor1))
# Se imprimen cadenas entonces transformo el booleano a cadena
# e.e, interesante, pero se imprimen como True o False
# Ya lo cambié :D