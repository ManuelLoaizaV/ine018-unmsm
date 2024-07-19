#paso el codigo que esta en el github a python

def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True


def letras():
    letra_a_morse = {""""" agrego valores en morse a cada respectiva letra como si fuera un mapa"""
        'A': ".-",
        'B': "-...",
        'C': "-.-.",
        'D': "-..",
        'E': ".",
        'F': "..-.",
        'G': "--.",
        'H': "....",
        'I': "..",
        'J': ".---",
        'K': "-.-",
        'L': ".-..",
        'M': "--",
        'N': "-.",
        'O': "---",
        'P': ".--.",
        'Q': "--.-",
        'R': ".-.",
        'S': "...",
        'T': "-",
        'U': "..-",
        'V': "...-",
        'W': ".--",
        'X': "-..-",
        'Y': "-.--",
        'Z': "--.."
    }


    morse_a_letra={v: k for k, v in letra_a_morse.items()}


    print("Traductor de código Morse")
    while True:
        entrada = input("> ")
        if esta_en_morse(entrada):
            palabras = entrada.split(' ')
            resultado = ''
            for palabra in palabras:
                if palabra:
                    letra = morse_a_letra.get(palabra)
                    if letra:
                        resultado += letra
            print(resultado)
        else:
            resultado = ''
            for c in entrada:
                if c == ' ':
                    continue
                morse = letra_a_morse.get(c.upper())
                if morse:
                    resultado += morse + ' '
            print(resultado)


letras()#llama a la funcion anterior xd
