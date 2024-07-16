def convertir_cadena():
    cadena = input("Ingrese una cadena: ")
    resultado = []
    
    for char in cadena:
        if resultado and resultado[-1].upper() == char.upper() and resultado[-1] != char:
            resultado.pop()
        else:
            resultado.append(char)
    
    return ''.join(resultado)

print(convertir_cadena())

