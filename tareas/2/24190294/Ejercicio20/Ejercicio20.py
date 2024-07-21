Abecedario_Morse = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..",
    'E': ".", 'F': "..-.", 'G': "--.", 'H': "....",
    'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---", 'P': ".--.",
    'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
    'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--.."
}

traductor_Morse = {v: k for k, v in Abecedario_Morse.items()}
entrada = input().strip()


if any(c.isdigit() or c.isalpha() for c in entrada):
    for letra in entrada.upper():
        if letra == ' ':
            print(end=' ')
        else:
            print(Abecedario_Morse.get(letra), end=' ')
else:
    palabras = entrada.split('  ')
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            print(traductor_Morse.get(letra), end='')

