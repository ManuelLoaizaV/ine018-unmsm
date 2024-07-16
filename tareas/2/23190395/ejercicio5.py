def morse():
    codigo_morse = {
        'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",
        'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
        'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
        'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
        'Y': "-.--", 'Z': "--.."
    }

    mensaje = input("Ingrese un mensaje: ").upper()
    m = [' '.join(codigo_morse.get(letra, '') for letra in mensaje)]
    
    return ' '.join(m)

print(morse())
