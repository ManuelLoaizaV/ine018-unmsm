from sympy import diff, solve, parse_expr, simplify
from sympy.abc import x

def derivada(funcion):
    deri = diff(funcion)
    deri = simplify(deri)
    return deri

#calculamos las derivadas
F = parse_expr('E**x*(x**2-5*x+6)')
derivada1 = derivada(F)
derivada2= derivada(derivada1)

#calculamos los puntos criticos
PC = solve(derivada2)
PC.sort()

#añadimos un valor más al punto cítico más alto
nuevo = derivada2.subs(x,PC[-1] +2)
PC.append(nuevo)
gaa= []

#calulamos la concavidad de cada intervalo
for p in PC:
    if derivada2.subs(x,p-1) >0:
        if p != PC[-1]:
            gaa.append(f"es de concavidad hacia arriba hasta cuando x = {p.evalf()}")
        else:
            gaa.append(f"es de concavidad hacia arriba hasta el infinito")
    else:
        if p != PC[-1]:
            gaa.append(f"es de concavidad hacia abajo hasta cuando x = {p.evalf()}")
        else:
            gaa.append(f"es de concavidad hacia abajo hasta el infnito")

for sol in gaa:
    print(sol)
print()
PC.pop()

#nos darán los puntos de inflexión pero no siempre estará desarrollado
for xd in PC:
    print("los puntos de inflexión son en x = ",xd)