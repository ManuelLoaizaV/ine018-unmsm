import sympy as sp

print ("Ejercicio 2:")
print ("Estudiar el dominio de la siguiente funcion:")

x = sp.symbols('x')

f = (sp.sqrt(4*x**2 - 3*x + 2) + sp.root(x - 2, 3)) / sp.sqrt(3*x**2 - x - 2)
sp.pprint (f)

dominio = sp.solveset(sp.denom(f) > 0, x, domain=sp.S.Reals)

print("")
print("Dominio de f(x):")
print(dominio)