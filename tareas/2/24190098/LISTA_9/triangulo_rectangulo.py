import math

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

def es_triangulo_rectangulo(x1, y1, x2, y2, x3, y3):
    a = distancia(x1, y1, x2, y2)
    b = distancia(x1, y1, x3, y3)
    c = distancia(x2, y2, x3, y3)

    return (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2)

def main():
   
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())

    if es_triangulo_rectangulo(x1, y1, x2, y2, x3, y3):
        print("El triángulo es rectángulo.")
    else:
        print("El triángulo no es rectángulo.")

main()
