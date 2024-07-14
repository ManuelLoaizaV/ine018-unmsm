def invertir_cadena(s):
    return s[::-1]

def convertir_a_buena(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entra:
        s = entra.read().strip()  

    caracteres = []
    for char in s:
        if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == char:
            caracteres.pop()
        else:
            caracteres.append(char)
    
    r = ''.join(caracteres)
    resultado_invertido = invertir_cadena(r)
    
    with open(archivo_salida, 'w') as sale:
        sale.write(resultado_invertido) 

convertir_a_buena('entrada17.txt', 'salida17.txt')
