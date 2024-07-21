import math
def calculate_h(a, b):
  h = math.sqrt(a**2 + b**2)
  return h
a = float(input("Ingrese el valor del primer cateto: "))
b = float(input("Ingrese el valor del segundo cateto: "))

h=calculate_h(a,b)
#Agregamos presición de 3 decimales para nuestro resultado de hipotenusa
print(f"La medida de la hipotenusa es : {h:.3f}")

