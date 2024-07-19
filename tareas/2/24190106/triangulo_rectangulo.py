import math

def distancia(x1 , y1 , x2 , y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

def triangulo_rectangulo(x1 , y1 , x2 , y2 , x3 , y3):
    a = distancia(x1 , y1 , x2 , y2)
    b = distancia(x2 , y2 , x3 , y3)
    c = distancia(x1 , y1 , x3 , y3)

    return a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a

x1 , y1 = 0 , 0
x2 , y2 = 3 , 0
x3 , y3 = 0 , 4
print(triangulo_rectangulo(x1 , y1 , x2 , y2 , x3 , y3))
