# el "encoding='utf-8'" sirve para poder utilizar la "ñ".
with open('Codigos_postales_entrada.txt', 'r', encoding='utf-8') as entrada:
    elementos = entrada.readlines()

# utilizo un diccionario "{ }" que funciona como mapa, donde asocio cada distrito con una lista "[ ]"
# de códigos postales correspondientes a dicho distrito con ":", utilizando "," para las separaciones.
codigos_postales = {
    "Breña": [15082, 15083],
    "Magdalena del Mar": [7021, 15076, 15086],
    "San Miguel": [15086, 15087, 15088],
    "Pueblo Libre": [15083, 15084, 15086, 15088],
    "Jesus María": [2002, 15072, 15073, 15076, 15084],
    "Lima": [7006, 15001, 15003, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001]
} 

distritos = {}
# "distrito" es {llave} y "codigos" es valor (lista de códigos postales) en el mapa "codigos_postales".
# donde, a su vez, definimos el "first" y el "second" del mapa (súper útil). :) 
# Nota: si no hubiera usado ".items()", hubiese obtenido la llave, pero no los valores asociados.
for distrito, codigos_postales_en_distritos in codigos_postales.items():
    for codigo in codigos_postales_en_distritos:
        if codigo in distritos:
            distritos[codigo].append(distrito)
        else:
            distritos[codigo] = [distrito] #creamos una lista asociada a "codigo" (donde estarán los distritos).

with open('Codigos_postales_salida.txt', 'w') as salida:
    for entrada in elementos:
        entrada = entrada.strip() # Para eliminar espacios en blanco al final y al inicio para no alterarlo.
        
        salida.write("> " + entrada.strip() + "\n")
        
        if entrada.isdigit(): #isdigit funciona como bool directamente, lo que ahorra la función análoga usada.
            codigo = int(entrada)
            if codigo in distritos:
                for distrito in distritos[codigo]:
                    salida.write(distrito + "\n")
            else:
                salida.write("El código no existe." + "\n")
        else:
            if entrada in codigos_postales:
                for codigo in codigos_postales[entrada]:
                    salida.write(str(codigo) + "\n")
            else:
                salida.write("El distrito no existe." + "\n")