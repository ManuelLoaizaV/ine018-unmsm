def invertir_cadena(s):
    return s[::-1]

def convertir_a_buena(s):
    caracteres = []
    for char in s:
        if (caracteres and caracteres[-1].islower() and 
                caracteres[-1].upper() == char):
            caracteres.pop()
        else:
            caracteres.append(char)
    
    r = ''.join(caracteres)
    return invertir_cadena(r)

if __name__ == "__main__":
    cadena = input()
    resultado = convertir_a_buena(cadena)
    print(resultado)