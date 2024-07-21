def procesar_cadena():
    m = input()  
    resultado = ""  

    for char in m:  # Recorrer cada carácter en la cadena de entrada
        if resultado and resultado[-1].islower() and resultado[-1].upper() == char:
            resultado = resultado[:-1]  # Sacar el último carácter de la cadena 
        else:
            resultado += char  # Sumamos a char al final de la cadena resultado

    return resultado  
print(procesar_cadena())  