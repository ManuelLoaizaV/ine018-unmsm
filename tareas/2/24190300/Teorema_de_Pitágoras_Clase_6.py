import math

# Notas antes de decidir hacerlo por archivo txt xd:
# Podría relacionar al "input" con "cin" y al "print" con "cout".
# Resulta más sencillo porque puedo inicializar, imprimir y leer en una sola línea, y no necesito colocar el
# tipo de varible al hacer esto.
# Al leer en el input, siempre retorna una cadena; sin embargo, es bastante fácil convertir la cadena 
# a un "int" o un "float", lo que puede ahorrarme muchas funciones de conversión que usaba en C++.
# Para realizar las continuaciones de lo que quieres imprimir en el print, ya no usas "<<", sino ",".

with open('Pitagoras_entrada.txt', 'r') as entrada:
    cateto_1 = float(entrada.readline())
    cateto_2 = float(entrada.readline()) 

# El "**" es bastante práctico.
cuadrado_1 = cateto_1 ** 2
cuadrado_2 = cateto_2 ** 2

# Parece que cuando llamas una función de una biblioteca determinada (módulo), tienes que acompañarla del 
# nombre de su biblioteca.
# Hay otras opciones, por ejemplo, cuando vas a utilizar muchas veces una misma función, puedes poner
# "from math import sqrt", así importas la función y no necesitas acompañarla de nada; asímismo, podrías
# podrías ponerle un alias a la biblioteca para que no resulte tan tedioso escribirla con "import math as m". 

resultado = math.sqrt(cuadrado_1 + cuadrado_2)

# Ví que era necesario que la salida sea un string (la coversión a string aplica la misma lógica que en los
# casos de float e int, con "str").
with open('Pitagoras_salida.txt', 'w') as salida:
    salida.write("El resultado es: " + str(resultado))

