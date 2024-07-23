import sympy as sp

print("Ejercicio 4 PC 2")
print("Desarrollar razonadamente dy / du , si se tienen las siguientes funciones: ")


x = sp.symbols('x')

g=  (1/(2* sp.sqrt(2)) )*sp.log(((x**2 - sp.sqrt(2) *x + 1)/(x**2 + sp.sqrt(2) *x + 1))) + (1/sp.sqrt(2)) * sp.atan( (sp.sqrt(2)*x)/(1 - x**2))
sp.pprint (g)

v= sp.diff(g,x)
dv= sp. simplify(v)
print("El valor de la derivada de dy es: ")
sp.pprint(dv)

f= sp.atan(( x**2 - 3) / (1 + 3 * (x**2)))
sp.pprint (f)

u= sp.diff(f,x)
df= sp.simplify(u)
print("El valor de la derivada de du es: ")
sp.pprint(df)

print("dy/du es :")

dy= v/u
dx= sp.simplify(dy)
sp.pprint(dx)

