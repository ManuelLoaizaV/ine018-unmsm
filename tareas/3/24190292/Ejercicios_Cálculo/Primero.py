#importamos las funcioens que necesitamos
from sympy import  real_root , diff, parse_expr, Pow, init_printing
from sympy.abc import x

init_printing(use_unicode=True)
# colocamos la función
Ec = parse_expr('((x-27)/(x+8)+sin(sin(4*x)**2)**3)**(1/3)')
#derivamos
derivada = diff(Ec)
derivadaencero = derivada.subs(x,0) #la derivada cuando x = 0
derivadaencero = real_root(derivadaencero) # lo colocamos en reales 
tangente = -Pow(derivadaencero,-1)# se calula la pendiente de la normal a partir de la derivada
# La ecuación de la recta es 0= m * x + b
Ecencero = Ec.subs(x,0) #b = función cuando x=0
#formamos la ecuación
Ecuacion = tangente*x + Ecencero 
Ecuacion = real_root(Ecuacion) # por si Encero tmb podria ser una solución complejo

print("La ecuación de la normal cuando x = 0 es:")
print('y = ',Ecuacion)
