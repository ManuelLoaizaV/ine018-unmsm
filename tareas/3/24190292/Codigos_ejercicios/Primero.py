#importamos las funcioens que necesitamos
from sympy import  real_root , diff, parse_expr, Pow
from sympy.abc import x

# colocamos la función
Ec = parse_expr('((x-27)/(x+8)+sin(sin(4*x)**2)**3)**(1/3)')

#derivamos
derivada = diff(Ec)

#la derivada cuando x = 0
derivadaencero = derivada.subs(x,0) 

# lo colocamos en reales
derivadaencero = real_root(derivadaencero)  

# se calula la pendiente de la normal a partir de la derivada
tangente = -Pow(derivadaencero,-1)

# La ecuación de la recta es 0= m * x + b

#b = función cuando x=0
Ecencero = Ec.subs(x,0)

#formamos la ecuación
Ecuacion = tangente*x + Ecencero 

# por si Encero tmb podria ser una solución complejo
Ecuacion = real_root(Ecuacion) 

print("La ecuación de la normal cuando x = 0 es:")
print(f"y = {Ecuacion}")
