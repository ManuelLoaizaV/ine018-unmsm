import sympy as sp

print ("Ejercicio 4:")
print ("Calcular el dominio, las simetrías y la composición de las funciones en los dos sentidos:")

x = sp.symbols('x')
f = x / (3*x**2 - 3)
g = sp.sqrt(x**2 + 2*x)

print ("f(x) =")
sp.pprint (f)
print ("")
print ("g(x) =")
sp.pprint (g)
print ("")

dominio_f = sp.solveset(sp.denom(f) != 0, x, domain=sp.S.Reals)
dominio_f = dominio_f - {-1, 1}

print("Dominio de f(x):")
print(dominio_f)

simetria_par_f = f.subs(x, -x) == f
if simetria_par_f:
    print("f(x) es par porque f(-x) = f(x)")
else:
    print("f(x) no es par")

simetria_impar_f = f.subs(x, -x) == -f
if simetria_impar_f:
    print("f(x) es impar porque f(-x) = -f(x)")
else:
    print("f(x) no es impar")

dominio_g = sp.solveset(x**2 + 2*x >= 0, x, domain=sp.S.Reals)

print("Dominio de g(x):")
print(dominio_g)

simetria_par_g = g.subs(x, -x) == g
if simetria_par_g:
    print("g(x) es par porque g(-x) = g(x)")
else:
    print("g(x) no es par")

simetria_impar_g = g.subs(x, -x) == -g
if simetria_impar_g:
    print("g(x) es impar porque g(-x) = -g(x)")
else:
    print("g(x) no es impar")

composicion_fg_f = f.subs(x, g)
print("Composición f(g(x)):")
sp.pprint(composicion_fg_f)
print ("")

composicion_gf_g = g.subs(x, f)
print("Composición g(f(x)):")
sp.pprint(composicion_gf_g)
print ("")