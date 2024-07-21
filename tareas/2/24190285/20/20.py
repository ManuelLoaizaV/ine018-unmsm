def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True

letra_a_morse = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",
    'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
    'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--.."
}

morse_a_letra = {}
for letra, codigo in letra_a_morse.items():
    morse_a_letra[codigo] = letra


with open('20entrada.txt', 'r') as entrada:
    lineas = entrada.readlines()

lineas_traducidas = []
for linea in lineas:
    linea = linea.strip()
    if esta_en_morse(linea):
        palabras = linea.split('  ')
        traduccion = []
        for palabra in palabras:
            letras = palabra.split()
            traduccion.append(''.join(morse_a_letra[letra] for letra in letras))
        lineas_traducidas.append(' '.join(traduccion))
    else:
        resultado = []
        for c in linea.upper():
            if c == ' ':
                continue
            resultado.append(letra_a_morse.get(c, ''))
        lineas_traducidas.append(' '.join(resultado))
with open('20salida.txt', 'w') as salida:
    for linea_traducida in lineas_traducidas:
        salida.write(linea_traducida + '\n')