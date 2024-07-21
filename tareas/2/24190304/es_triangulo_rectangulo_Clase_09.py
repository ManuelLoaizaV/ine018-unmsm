import math
#No me complique mucho en este ejercicio ya que como ya tenia la formula y 
# la estructura en c++, me quedo muy claro lo que es que aca no se utiliza codigo para elevar solo se coloca**
# Verdad tambien en vez de colocar 1 o 0 como en c++, aca lo hice con true o false
def Distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)

def EsTrianguloRectangulo(x1, y1, x2, y2, x3, y3):
    a = Distancia(x1, y1, x2, y2)
    b = Distancia(x1, y1, x3, y3)
    c = Distancia(x2, y2, x3, y3)


    return (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2)


print(EsTrianguloRectangulo(0, 0, 0, 3, 4, 0))  
print(EsTrianguloRectangulo(0, 0, 0, 3, 4, 1)) 