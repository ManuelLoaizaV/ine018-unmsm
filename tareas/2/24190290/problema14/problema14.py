def cadena_a_entero(s):
   
    n = len(s)

    entero = 0

    inicio = 0
    if s[0] == '-':
        inicio = 1


    for i in range(inicio, n):
        entero = 10 * entero + int(s[i])

    if s[0] == '-':
        entero *= -1

    return entero

with open('entrada14.txt', 'r') as entrada, open('salida14.txt', 'w') as salida:
   
    lineas = entrada.readlines()

    
    for linea in lineas:
        cadena = linea.strip()  
        resultado = cadena_a_entero(cadena)
        salida.write(f"{resultado}\n")

salida.write(f"Se han procesado las cadenas del archivo '{'entrada14.txt'}' y se han escrito los resultados en '{'salida14.txt'}'.")
