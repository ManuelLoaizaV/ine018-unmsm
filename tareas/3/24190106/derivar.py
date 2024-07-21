import sympy as sp

x=sp.symbols('x')

y=(x**2 + 2*x)

d=sp.diff(y,x)

print(d)

