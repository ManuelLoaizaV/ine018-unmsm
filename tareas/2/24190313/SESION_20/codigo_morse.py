def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True
letra_a_morse = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
    'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",        
    'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
    'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
    'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."
}
morse_a_letra = {
    ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E',
    "..-.": 'F', "--.": 'G', "....": 'H', "..": 'I', ".---": 'J',
    "-.-": 'K', ".-..": 'L', "--": 'M', "-.": 'N', "---": 'O',
    ".--.": 'P', "--.-": 'Q', ".-.": 'R', "...": 'S', "-": 'T',
    "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X', "-.--": 'Y', "--..": 'Z'
}
print("Traductor de código Morse")
while True:
    entrada = input("> ").strip()
    if esta_en_morse(entrada):
        palabras = entrada.split('   ')
        mensaje = []
        for palabra in palabras:
            letras = palabra.split()
            traduccion = ''.join([morse_a_letra.get(letra, '') for letra in letras])
            mensaje.append(traduccion)
        print(' '.join(mensaje))
    else:
        resultado = []
        for caracter in entrada.upper():
            if caracter == ' ':
                resultado.append('   ')
            else:
                resultado.append(letra_a_morse.get(caracter, ''))
        print(' '.join(resultado))