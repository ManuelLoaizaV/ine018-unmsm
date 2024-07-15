a_morse = {
    'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".", 
    'F': "..-.",   'G': "--.",    'H': "....",   'I': "..",     'J': ".---", 
    'K': "-.-",    'L': ".-..",   'M': "--",     'N': "-.",     'O': "---", 
    'P': ".--.",   'Q': "--.-",   'R': ".-.",    'S': "...",    'T': "-", 
    'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",   'Y': "-.--", 
    'Z': "--.."
}

print("ESCRIBIR TEXTO PARA TRADUCIR ")
while True: #Bucle para tener más entradas
    entrada = input("> ").strip() #Pedir entrada y eliminar espacios en blanco
    if all(c in '-. ' for c in entrada):#Vemos si la entrada es código morse
        resultado = ''.join(a_morse.get(codigo, '?') for codigo in entrada.split()) #Convertir de morse a letras
    else:
        resultado = ' '.join(a_morse[letra] for letra in entrada.upper() if letra in a_morse) #Convertir de letras a morse
    print(resultado)