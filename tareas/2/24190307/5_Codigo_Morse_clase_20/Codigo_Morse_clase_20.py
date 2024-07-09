diccionario = {}
    # Vacio... 
diccionario["A"] = ".-"
diccionario["B"] = "-..."
diccionario["C"] = "-.-."
diccionario["D"] = "-.."
diccionario["E"] = "."
diccionario["F"] = "..-."
diccionario["G"] = "--."
diccionario["H"] = "...."
diccionario["I"] = ".."
diccionario["J"] = ".---"
diccionario["K"] = "-.-"
diccionario["L"] = ".-.."
diccionario["M"] = "--"
diccionario["N"] = "-."
diccionario["O"] = "---"
diccionario["P"] = ".--."
diccionario["Q"] = "--.-"
diccionario["R"] = ".-."
diccionario["S"] = "..."
diccionario["T"] = "-"
diccionario["U"] = "..-"
diccionario["V"] = "...-"
diccionario["W"] = ".--"
diccionario["X"] = "-..-"
diccionario["Y"] = "-.--"
diccionario["Z"] = "--.."

diccionario_invertido = {valor: llave for llave, valor in diccionario.items()}
# Dale sí comprendí eso, se parece a c++ en cierta forma

def es_morse(letra):
    for char in letra:
        if char.isalpha():
            return False
    return True

def traductor(string):
    traduccion = ""
    # Void >.<

    if es_morse(string):
        palabras_morse = string.split()
        for palabra in palabras_morse:
            if palabra in diccionario_invertido:
                traduccion += diccionario_invertido[palabra]
                
    else:
        for char in string:
            if char in diccionario:
                traduccion += diccionario[char] + " "
            
    return traduccion.strip()

with open("Codigo_Morse_entrada.txt", "r") as entrada:
    frase = entrada.readline()
    frase2 = entrada.readline()
    frase3 = entrada.readline()

resultado = traductor(frase)
resultado1 = traductor(frase2)
resultado2 = traductor(frase3)

with open("Codigo_Morse_salida.txt", "w") as salida:
    salida.write("> Traducción: " + str(resultado) + "\n" +
                 "> Traducción: " + str(resultado1) + "\n" +
                 "> Traducción: " + str(resultado2))