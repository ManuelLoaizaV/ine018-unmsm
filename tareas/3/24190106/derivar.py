import sympy as sp
#me costó bastante instalarla
x=sp.symbols('x')
#con sp.symbols por lo que entendi es que declara al x como variable
y=(x**2 + 2*x)
#aca creo mi funcion f(x)=y
d=sp.diff(y,x)
#aca derivo mi funcion y lo igualo a d
print(d)
# y finalmente imprimo el resultado de la derivada
