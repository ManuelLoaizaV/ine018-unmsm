with open('Mayusculas_entrada.txt', 'r') as entrada:
    cadena = entrada.readline()

# len = size
n = len(cadena)

# No puedo utilizar un for para iterar los caracteres de las cadenas porque las cadenas en Python 
# son objetos inmutables, quiere decir, no puedo modificar los caracteres individuales de una 
# cadena directamente. 
# La solución es utilizar funciones específicas que relacionen los caracteres con su orden en ASCII y
# generar nuevos caracteres que reemplacen los anteriores a partir de eso, agregándolos a una lista.

# Creación de una lista vacía.
lista_de_mayusculas = []
for i in range(n):
# "ord" arroja la posición que ocupa el caracter en ASCII, algo bastante útil después de ver que no puedo
# no se pueden modificar los caracteres de forma directa usando ASCII.
    caracter = ord(cadena[i])
    if 97 <= caracter <= 122:
        # El chr funciona similar al ord, solo que en sentido opuesto.
        caracter_nuevo = chr(caracter - 32)
        lista_de_mayusculas.append(caracter_nuevo)
    else:
        lista_de_mayusculas.append(cadena[i])

# Veo el siguiente código muy útil, ya que no solo me permite unir los elementos de una lista en una cadena,
# sino que me permite elegir lo que quiero que haya entre dichos elementos. En este caso, coloqué una cadena
# vacía, indicando que deseo que se lea de corrido. 
# También noté que tanto " " como ' ' son válidas para las cadenas.
cadena_final = ''.join(lista_de_mayusculas)

with open('Mayusculas_salida.txt', 'w') as salida:
    salida.write(cadena_final)
