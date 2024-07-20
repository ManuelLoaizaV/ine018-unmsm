# Sympy
Antes de usar se debe instalar sympy. Se puede hacer directamente desde VSC
Se debe colocar el siguiente comando [pip install sympy]para instalar y 
automáticamente sympy se "acomodará" en todos los sitios que se requiera.
## ¿Cómo funciona Sympy?
Sympy es una biblioteca que se usa mayormente en expresiones matemáticas
usando para ello expresiones simbólicas si se requiere, usa algoritmos para
ejecutar sus distintas funciones.

A expresiones simbólicas me refiero a la representacion de variables x,y 
por ejemplo en polinomios [2*x + y] y no solo que arroje números. 
```py
>>>from sympy import symbols
>>>x, y = symbols('x y')
>>>expr = x + 2*y
>>>expr
x + 2*y
```
En el ejemplo anterior como [x] ni [y] estaban evaluados solo colocó su simbolo.

Pero también podemos aclarar los "predicados" de cada variables como decir 
que es posito, racional, entero, etc.
```py
>>>from sympy import symbols
>>>x = symbols('x', negative = True)
```
Hemos aclarado que [x] será negativo.

Si es que no se quiere variables, se puede fácilmente reemplazar por un valor 
numérico que queramos, repito sympy tiene un sinfin de funciones, que podemos 
usar para crear muchas más funciones que necesitemos.

Toda la documentación de [*sympy*](https://docs.sympy.org/latest/index.html)
está documentado.

## ¿Como funciona Sympy en mis códigos?
He usado solo funciones básicas de cálculo como symbols, subs que sustituye el
valor de una variable, parse_expr que convierte una cadena a expresion matemática.
Incluso cuando no declaremos una función como [sin] e incluso calcular su [sin]
Pero primero declaramos la variable x como [sympy.abc].
```py
>>>from sympy import parse_expr
>>>from sympy.abc import x
>>> ex = parse_expr('sin(x)')
>>> ex
sin(x)
>>> ex.subs(x,4)
sin(4)
>>> ex.subs(x,4).evalf()
-0.756802495307928
```
[evalf] se usa para encontrar el número y no solo su representación.

Además de cálculos sencillos usando [diff] que calula la derivada de un polinomio.
Se usó [solve] para poder encontrar las soluciones a polinomios.

También [real_root] para encontrar la solución real de una expresión si es que pueden salir
soluciones complejas.
```py
>>>from sympy import parse_expr
>>>from sympy.abc import x
>>>eq = (x)**(1/3)
>>>eq
x**0.333333333333333
>>>eq.nsimplify()
x**(1/3)
>>>real_root(eq.nsimplify().subs(x,-1))
-1
```
[nsimplify] para hacer que se represente mediante un numero racional el exponente, pues 
hace lo contrario a simplificar.