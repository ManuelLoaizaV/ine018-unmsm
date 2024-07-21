import sympy as sp
x = sp.symbols('x')
# Defino mi función
f = (sp.sqrt(4*x**2 - 3*x + 2) + sp.root(x - 2, 3)) / sp.sqrt(3*x**2 - x - 2)
print("2. Estudiar el dominio de la siguiente función: ")
print("f(x) = ")
sp.pprint(f)

# Hallando dominio
dominio = sp.solveset(sp.denom(f)>0, x, domain=sp.S.Reals)

print()
print("El dominio de la función es: ")
print(dominio)
