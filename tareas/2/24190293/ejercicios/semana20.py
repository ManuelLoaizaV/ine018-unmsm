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

morse_a_letra = { codigo : letra for letra, codigo in letra_a_morse.items()}
print ("--- Traductor de codigo morse ---")
while True:
    entrada = input(">> ")
    
    es_morse = True
    for c in entrada:
        if c == ' ':
            continue
        if c.isalpha():
            es_morse = False
            break
        
    if es_morse:
        i = 0
        while i < len(entrada):
            if entrada[i] in ['.', '-']:
                j = i
                while j < len(entrada) and entrada[j] in ['.', '-']:
                    j = j + 1
                codigo = entrada [i:j]
                print(morse_a_letra.get(codigo, ''), end = '')
                i = j
            else:
                i = i + 1
    else:
        for c in entrada:
            if c == ' ':
                continue
            print (letra_a_morse.get(c.upper(), ''), end = ' ')
    print()