LETRA_A_MORSE = {
    'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".", 
    'F': "..-.",   'G': "--.",    'H': "....",   'I': "..",     'J': ".---", 
    'K': "-.-",    'L': ".-..",   'M': "--",     'N': "-.",     'O': "---", 
    'P': ".--.",   'Q': "--.-",   'R': ".-.",    'S': "...",    'T': "-", 
    'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",   'Y': "-.--", 
    'Z': "--.."
}

def morse_a_letras(morse):
    letras = []
    for codigo in morse.split():
        letra = LETRA_A_MORSE.get(codigo, '?')
        letras.append(letra)
    return ''.join(letras)

def letras_a_morse(letras):
    morse = []
    for letra in letras.upper():
        if letra in LETRA_A_MORSE:
            morse.append(LETRA_A_MORSE[letra])
    return ' '.join(morse)

def main():
    print(" INSERTE LO QUE QUIERE TRADUCIR A MORSE ")
    while True:
        entrada = input("> ").strip()
        if all(c in '-. ' for c in entrada):
            resultado = morse_a_letras(entrada)
            print(resultado)
        else:
            resultado = letras_a_morse(entrada)
            print(resultado)

if __name__ == "__main__":
    main()
