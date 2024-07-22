import sympy as sp
print(" Determinar la continuidad y derivabilidad de la siguiente función:")
x= sp.Symbol('x')
f1= (1/x)+1 
ex_st= sp.pretty(f1)
print ( f"{ex_st}; si x < 0 " ) 
f2= x**3  
ext_st2= sp.pretty(f2)  
print(f"{ext_st2}; si  0 <= x < 2 ")
f3= 3*x +2  
ext_st3= sp.pretty(f3)
print(f"{ext_st3}; si  x>=2 ")

print("SOLUCION:")
print("1. Aplicamos limites laterales")
print("2. Si comprobamos que los limites son iguales, entonces es continua")
print("3. Despues de saber que es continua, se prueba su derivabilidad")

print(" LIMITES LATERALES EN x=0")
print(" Limite cuando x---> 0-")

v1=sp.limit(f1, x , 0, dir='-')
print("Es:")
sp.pprint(v1)
print(" Limite cuando x---> 0+")

v2=sp.limit(f2, x , 0, dir='+')
print("Es:")
sp.pprint(v2)
print(" Los limites laterales de 0 no son iguales, por lo tanto no es continua, y si no es continua no es derivable.")

print(" LIMITES LATERALES DE x=2")
print(" Limites cuando x---> 2-")

s1=sp.limit(f2 , x , 2, dir='-')
print("Es:")
sp.pprint(s1)

print(" Limites cuando x---> 2+")
s2=sp.limit(f3 , x , 2, dir='-')
print("Es:")
sp.pprint(s2)
print( "Los limites laterales de 2 son iguales, por lo tanto es continua, ahora pasaremos a derivarlo.")

print(" DERIVANDO LAS FUNCIONES CONTINUAS")
print( f"La derivada de {f2} es:")
c1= sp.diff(f2)
sp.pprint(c1)

print(f"La derivada de {f3} es:")
c2=sp.diff(f3)
sp.pprint(c2)
print("Reemplazando el valor de x")

r= c1.subs(x,2)
s= c2.subs(x,2)

print(f"El valor de {c1} es: {r}")
print(f"El valor de {c2} es: {s}")

print("Las derivadas laterales no son iguales asi que no son derivables.")



