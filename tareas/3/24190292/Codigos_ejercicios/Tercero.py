#importamos las funciones
from sympy import diff, parse_expr, pprint
from sympy.abc import x,y

F = parse_expr('x**2*sin(x+y)-5*y*E**x-3/sqrt(7)')
#queremos saber su derivada implícita

#calculamos la derivada conj respecto a x, y
derivadax = diff(F,x)
derivaday = diff(F,y)

#calculamos por divisiones
dy_dx = (-1)*derivadax/derivaday

pprint(dy_dx)

