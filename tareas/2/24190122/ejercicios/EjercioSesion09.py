
#¿Es triangulo rectangulo?
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** 0.5

def esTrectangulo(x1, y1, x2, y2, x3, y3):
    a = distancia(x1, y1, x2, y2)
    b = distancia(x1, y1, x3, y3)
    c = distancia(x2, y2, x3, y3)

    return (a**2 + b**2 == c**2 or
            a**2 + c**2 == b**2 or
            c**2 + b**2 == a**2)

print(esTrectangulo(0, 0, 0, 3, 4, 0))
print(esTrectangulo(0, 0, 0, 3, 4, 1))
