def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True
letra_a_morse = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--.."
}
morse_a_letra = {codigo: letra for letra, codigo in letra_a_morse.items()}

def esta_en_morse(cadena):
    # Asume que una cadena está en Morse si contiene '.' o '-'
    return all(c in ['.', '-', ' '] for c in cadena)

print("Traductor de código Morse")
while True:
    entrada = input("> ")

    if esta_en_morse(entrada):
        i = 0
        while i < len(entrada):
            if entrada[i] == '.' or entrada[i] == '-':
                j = i
                while j < len(entrada) and (entrada[j] == '.' or entrada[j] == '-'):
                    j += 1
                codigo = entrada[i:j]
                if codigo in morse_a_letra:
                    print(morse_a_letra[codigo], end='')
                i = j
            else:
                i += 1
    else:
        for c in entrada:
            if c == ' ':
                continue
            if c.upper() in letra_a_morse:
                print(letra_a_morse[c.upper()], end=' ')
    print()
