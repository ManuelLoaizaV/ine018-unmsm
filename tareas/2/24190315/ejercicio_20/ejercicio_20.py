def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True

def codigo_morse():
    letra_a_morse = {
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

    morse_a_letra = {v: k 
                    for k, v in letra_a_morse.items()
                    }

    print("Traductor de código Morse")
    while True:
        entrada = input("> ")
        if esta_en_morse(entrada):
            i = 0
            while i<len(entrada):
                if entrada[i] == '.' or entrada[i] == '-':
                    j = i
                    while j<len(entrada) and (entrada[j] == '.' or entrada[j] == '-'):
                        j = j + 1
                    codigo = entrada[i:j]
                    print(morse_a_letra[codigo], end = '')
                    i = j
                else:
                    i = i + 1
        else:
            for c in entrada:
                if c == ' ':
                    continue
                print(letra_a_morse[c.upper()], end = ' ')
        
        print()
codigo_morse()