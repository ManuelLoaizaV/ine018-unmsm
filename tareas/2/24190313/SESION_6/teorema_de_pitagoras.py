import math
def hipotenusa(a,b):
    c = float(math.sqrt((a*a)+(b*b)))
    return c
a = float(input("Ingrese el valor del primer cateto: "))
b = float(input("Ingrese el valor del segundo cateto: "))
print (f"Por el teorema de Pitágoras, la hipotenusa mide: {hipotenusa(a,b)}")