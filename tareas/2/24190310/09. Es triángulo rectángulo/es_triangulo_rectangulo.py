import math

def distancia(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    return math.sqrt(dx*dx + dy*dy)

def es_triángulo_rectángulo(x1, y1, x2, y2, x3, y3):
    a=distancia(x1, y1, x2, y2)
    b=distancia(x1, y1, x3, y3)
    c=distancia(x2, y2, x3, y3)

    return a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a

def main():
  print(es_triángulo_rectángulo(0, 0, 0, 3, 4, 0))
  print(es_triángulo_rectángulo(0, 0, 0, 3, 4, 1))
if __name__ == "__main__":
   main()