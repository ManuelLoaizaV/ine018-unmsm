def EstaEnMorse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True

if __name__ == "__main__":
    letra_a_morse ={
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..', 
    }
    morse_a_letra = {v: k for k, v in letra_a_morse.items()}

    print("Bienvenidos a ''Traducciones de código morse'' ")
    print()
    while True:
        entrada = input("> ").strip()

        if EstaEnMorse(entrada):
            palabras = entrada.split('  ')
            traduccion = []
            for palabra in palabras:
                letras = palabra.split()
                traduccion.append(''.join(morse_a_letra[letra] for letra in letras))
            print(' '.join(traduccion))
        else:
            traduccion = []
            for c in entrada.upper():
                if c == ' ':
                    continue
                traduccion.append(letra_a_morse.get(c, '/'))
            print(' '.join(traduccion))