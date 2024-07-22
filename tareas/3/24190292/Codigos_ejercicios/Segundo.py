#importamos las funciones
from sympy import simplify, diff, parse_expr, pprint
from sympy.abc import x

#colocamos la función
F = parse_expr('1/(2*sqrt(2))*ln((x**2-sqrt(2)*x+1)/(x**2+sqrt(2)*x+1)) + 1/(sqrt(2))*atan(sqrt(2)*x/(1-x**2))')

#Calculamos la derivada y la simplificamos
derivadaF = diff(F,x)
derivadaF = simplify(derivadaF)

#colocamos la segunda función y repetimos
U = parse_expr('atan((x**2-3)/(1+3*x**2))')
derivadaU = diff(U,x)
derivadaU = simplify(derivadaU)

#Calculamos lo que nos piden 
dy_du = derivadaF/derivadaU

pprint(dy_du)

