import math

def Distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def EsTrianguloRectangulo(x1, y1, x2, y2, x3, y3):
    lado1 = Distancia(x1, y1, x2, y2)
    lado2 = Distancia(x2, y2, x3, y3)
    lado3 = Distancia(x3, y3, x1, y1)
    hipotenusa = max(lado1, lado2, lado3)
    cuadrado_de_catetos = lado1**2 + lado2**2 + lado3**2 - hipotenusa**2
    if hipotenusa**2 == cuadrado_de_catetos:
        return True
    else:
        return False

x1 = float(input("Vértice X1: "))
y1 = float(input("Vértice Y1: "))
x2 = float(input("Vértice X2: "))
y2 = float(input("Vértice Y2: "))
x3 = float(input("Vértice X3: "))
y3 = float(input("Vértice Y3: "))
print(EsTrianguloRectangulo(x1, y1, x2, y2, x3, y3))
