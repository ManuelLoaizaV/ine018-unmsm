from sympy import symbols, init_printing, Integral
from IPython.display import display
# Definir variables y una expresión
x, y = symbols('x y')
expr = Integral(x**2 + y**2, (x, 0, 1))

# Sin init_printing


# Con init_printing
init_printing(use_unicode=True)


archivogaaa= 'pruebasalida.txt'
with open(archivogaaa, 'w') as archivo:
    archivo.write("holasgnjksegksegnlksejghsejkghkseth\n wrtwetwetewt")
