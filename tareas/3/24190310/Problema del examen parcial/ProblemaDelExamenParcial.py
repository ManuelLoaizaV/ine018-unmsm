import sympy as sp
x = sp.symbols('x')

# Defino mi función
f = ((sp.sqrt(2+(sp.root(x, 5))))-2)/(x-32)
print("4. Sea la función f(x) = ")
sp.pprint(f)
print("¿Cómo debe ser definida f(32) para que la función sea continua en x=32?")

# Hallo el límite
limite = sp.limit(f, x, 32)

print()
print("El límite de la función es: ")
print(limite)