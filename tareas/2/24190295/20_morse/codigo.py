def morse():
    codigo_morse = {
        'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".",      'F': "..-.",
        'G': "--.",    'H': "....",   'I': "..",     'J': ".---",   'K': "-.-",    'L': ".-..",
        'M': "--",     'N': "-.",     'O': "---",    'P': ".--.",   'Q': "--.-",   'R': ".-.",
        'S': "...",    'T': "-",      'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",
        'Y': "-.--",   'Z': "--.."
    }

    mensaje = input().upper()

    m = []
  #agregas elementos con append
    for letra in mensaje:
        if letra == ' ':
            m.append('')
        
        else:
            m.append(codigo_morse.get(letra, ''))
#se concatena elemento
    return ' '.join(m)

print(morse())
# se simplifica el codigo

