import sympy as sp
from itertools import product

print ("Ejercicio 1:")
print ("Sean:")
print ("A = {x ∈ Z / (x^2 - 1)(3x^2 - 6x) = 0}")
print ("B = {x ∈ N / (x^2 - 7x + 6)(x^2 - 4) = 0}")
print ("R1 = {(x;y) ∈ AxB / x - y = 0}")
print ("R2 = {(x;y) ∈ AxB / x > y}")
print ("R3 = {(x;y) ∈ BxB / x + y = 7}")
print ("Determinar:")
print ("I) (Dom.R1 U Dom.R2) Δ (Rang.R1 U Rang.R3)")
print ("II) (Rang.(R1 ∩ R2) - Dom.(R1 U R3))")

x = sp.symbols('x')

A_eq = (x**2 - 1)*(3*x**2 - 6*x)
B_eq = (x**2 - 7*x + 6)*(x**2 - 4)

A_soluciones = sp.solve(A_eq, x)
B_soluciones = sp.solve(B_eq, x)

A = [sol for sol in A_soluciones if sol.is_integer]
B = [sol for sol in B_soluciones if sol.is_nonnegative and sol.is_integer]

print(f'A = {A}')
print(f'B = {B}')

R1 = [(a, b) for a, b in product(A, B) if a - b == 0]
R2 = [(a, b) for a, b in product(A, B) if a > b]
R3 = [(a, b) for a, b in product(B, B) if a + b == 7]

print(f'R1 = {R1}')
print(f'R2 = {R2}')
print(f'R3 = {R3}')

Dom_R1 = {x for x, y in R1}
Rang_R1 = {y for x, y in R1}

Dom_R2 = {x for x, y in R2}
Rang_R2 = {y for x, y in R2}

Dom_R3 = {x for x, y in R3}
Rang_R3 = {y for x, y in R3}

print(f'Dom(R1) = {Dom_R1}')
print(f'Rang(R1) = {Rang_R1}')
print(f'Dom(R2) = {Dom_R2}')
print(f'Rang(R2) = {Rang_R2}')
print(f'Dom(R3) = {Dom_R3}')
print(f'Rang(R3) = {Rang_R3}')

Dom_R1_union_Dom_R2 = Dom_R1.union(Dom_R2)
Rang_R1_union_Rang_R3 = Rang_R1.union(Rang_R3)
resultado_I = Dom_R1_union_Dom_R2.symmetric_difference(Rang_R1_union_Rang_R3)
print(f"I) (Dom.R1 U Dom.R2) Δ (Rang.R1 U Rang.R3) = {resultado_I}")

Rang_R1_inter_Rang_R2 = Rang_R1.intersection(Rang_R2)
Dom_R1_union_Dom_R3 = Dom_R1.union(Dom_R3)
resultado_II = Rang_R1_inter_Rang_R2.difference(Dom_R1_union_Dom_R3)
print(f"II) Rang.(R1 ∩ R2) - Dom.(R1 U R3) = {resultado_II}")