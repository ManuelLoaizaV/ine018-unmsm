import sympy as sp

print ("Ejercicio 5:")
print ("Dadas las funciones:")

x = sp.symbols('x')

h = sp.Piecewise(
    (x**2, x >= 1),
    (sp.Abs(x - 1), x < 1)
)

g = sp.Piecewise(
    (sp.sqrt(x + 1), x >= -1),
    (x**2 - 1, x < -1)
)

print ("h(x):")
sp.pprint (h)
print ("")

print ("g(x):")
sp.pprint (g)
print ("")

print("Determinar (h/g)(x) con su respectivo dominio")

h1 = x**2
h2 = sp.Abs(x - 1)
g1 = sp.sqrt(x + 1)
g2 = x**2 - 1

h1_g1 = (h1 / g1)
h1_g2 = (h1 / g2)
h2_g1 = (h2 / g1)
h2_g2 = (h2 / g2)

print ("h1/g1:")
sp.pprint(h1_g1)
print ("")
print ("h1/g2:")
sp.pprint(h1_g2)
print ("")
print ("h2/g1:")
sp.pprint(h2_g1)
print ("")
print ("h2/g2:")
sp.pprint(h2_g2)
print ("")

dom_h1 = sp.Interval(1, sp.oo)
dom_h2 = sp.Interval(-sp.oo, 1, right_open=True)
dom_g1 = sp.Interval(-1, sp.oo)
dom_g2 = sp.Interval(-sp.oo, -1, right_open=True)

def calcular_dominio(h_dom, g_dom, denom):
    inter_dom = h_dom.intersect(g_dom)
    ceros = sp.solveset(denom, x, domain=sp.S.Reals)
    final_dom = inter_dom - ceros
    return final_dom

dom_h1_g1 = calcular_dominio(dom_h1, dom_g1, g1)
dom_h1_g2 = calcular_dominio(dom_h1, dom_g2, g2)
dom_h2_g1 = calcular_dominio(dom_h2, dom_g1, g1)
dom_h2_g2 = calcular_dominio(dom_h2, dom_g2, g2)

print("Dominio de h1/g1:")
sp.pprint(dom_h1_g1)
print("Dominio de h1/g2:")
sp.pprint(dom_h1_g2)
print("Dominio de h2/g1:")
sp.pprint(dom_h2_g1)
print("Dominio de h2/g2:")
sp.pprint(dom_h2_g2)