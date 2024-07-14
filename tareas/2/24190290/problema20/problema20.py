def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True

def main():
    letra_a_morse = {
        'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".",      
        'F': "..-.",   'G': "--.",    'H': "....",   'I': "..",     'J': ".---",   
        'K': "-.-",    'L': ".-..",   'M': "--",     'N': "-.",     'O': "---",    
        'P': ".--.",   'Q': "--.-",   'R': ".-.",    'S': "...",    'T': "-",      
        'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",   'Y': "-.--",   
        'Z': "--.."
    }

    morse_a_letra = {v: k for k, v in letra_a_morse.items()}

    with open('entrada20.txt', 'r') as entra, open('salida20.txt', 'w') as sale:
        for line in entra:
            entrada = line.strip()

            if esta_en_morse(entrada):
                palabras = entrada.split(' ')
                traduccion = ''
                for palabra in palabras:
                    if palabra in morse_a_letra:
                        traduccion += morse_a_letra[palabra]
                sale.write(traduccion + '\n')
            else:
                for c in entrada:
                    if c == ' ':
                        continue
                    sale.write(letra_a_morse.get(c.upper(), '') + ' ')
                sale.write('\n')

main()
