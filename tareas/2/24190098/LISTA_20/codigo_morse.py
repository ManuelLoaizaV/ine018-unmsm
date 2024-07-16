def esta_en_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z': 
            return False
    return True

letra_a_morse = {
    'A':".-",
    'B':"-...",
    'C':"-.-.", 
    'D':"-..", 
    'E':".",
    'F':"..-.", 
    'G':"--.", 
    'H':"....", 
    'I':"..", 
    'J':".---",
    'K':"-.-", 
    'L':".-..", 
    'M':"--", 
    'N':"-.", 
    'O':"---",
    'P':".--.", 
    'Q':"--.-", 
    'R':".-.", 
    'S':"...", 
    'T':"-",
    'U':"..-", 
    'V':"...-", 
    'W':".--", 
    'X':"-..-", 
    'Y':"-.--",
    'Z':"--.."
}

morse_a_letra = {v: k for k, v in letra_a_morse.items()}

print("Traductor de código Morse")
while True:
    a = input("> ")

    if esta_en_morse(a):
        codigos = a.split(' ')
        resultado = ''.join(morse_a_letra.get(codigo, '') for codigo in codigos if codigo in morse_a_letra)
        print(resultado)
    else:
        resultado = ' '.join(letra_a_morse.get(c.upper(), '') for c in a if c != ' ')
        print(resultado)
