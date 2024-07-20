import math

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def intersectan_circulos(x1, y1, r1, x2, y2, r2):
    return distancia(x1, y1, x2, y2) <= r1 + r2

if __name__ == "__main__":
    print(intersectan_circulos(0, 0, 5, 0, 6, 2))
    print(intersectan_circulos(0, 0, 10, 50, 50, 10))