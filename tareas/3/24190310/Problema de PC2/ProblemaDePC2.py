import sympy as sp
x, y = sp.symbols('x y')

# Defino función
f = x**2 * sp.sin(x + y) - 5*y*sp.exp(x) - 3/(4*sp.sqrt(7))
print("5. Determinar razonadamente: dy/dx")
print("f(x, y) = ")
sp.pprint(f)

# Para derivación implícita
df_dx = sp.diff(f, x)  
df_dy = sp.diff(f, y)  

# Para dy/dx
dy_dx = -df_dx / df_dy
dy_dx = sp.simplify(dy_dx)

print()
f = ()
print(f"La derivación implícita es: ")
sp.pprint(dy_dx)