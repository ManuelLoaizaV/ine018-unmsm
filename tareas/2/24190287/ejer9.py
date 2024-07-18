def interseccion(m1, b1, m2, b2):
    if m1 == m2:
        return None  
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)

def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def CalcularAreaEntreLasRectas(m1, b1, m2, b2, m3, b3):

    p1 = interseccion(m1, b1, m2, b2)
    p2 = interseccion(m2, b2, m3, b3)
    p3 = interseccion(m3, b3, m1, b1)

    if p1 is None or p2 is None or p3 is None:
        return 0.0
    
    a = distancia(p1, p2)
    b = distancia(p2, p3)
    c = distancia(p3, p1)
    s = area(a, b, c)
    print(s)

m1 = float(input())
b1 = float(input())
m2 = float(input())
b2 = float(input())
m3 = float(input())
b3 = float(input())

CalcularAreaEntreLasRectas(m1, b1, m2, b2, m3, b3)