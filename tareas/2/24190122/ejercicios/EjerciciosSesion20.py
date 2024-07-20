# Diccionario de traducción de letra a código Morse
letra_a_morse = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",
    'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
    'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--..",
    '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-", 
    '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----."
}

# Función para traducir texto a código Morse
def texto_a_morse(texto):
    morse = []
    for caracter in texto.upper():
        if caracter in letra_a_morse:
            morse.append(letra_a_morse[caracter])
            morse.append(' ')  # Separador entre letras
        elif caracter == ' ':
            morse.append('/')  # Separador entre palabras
    return ''.join(morse)

# Función para traducir código Morse a texto
def morse_a_texto(morse):
    texto = []
    palabras = morse.split('/')
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            for key, value in letra_a_morse.items():
                if value == letra:
                    texto.append(key)
                    break  # Salir del bucle interno
        texto.append(' ')  # Separador entre palabras
    return ''.join(texto)

# Función principal para interactuar con el usuario
def main():
    print("Bienvenido al traductor de código Morse")

    while True:
        opcion = input("Elija una opción:\n  1. Texto a Morse\n  2. Morse a Texto\n  3. Salir\n> ")

        if opcion == '1':
            texto = input("Ingrese el texto a convertir a Morse: ")
            morse = texto_a_morse(texto)
            print(f"Texto en Morse: {morse}")
        elif opcion == '2':
            morse = input("Ingrese el código Morse a convertir a texto: ")
            texto = morse_a_texto(morse)
            print(f"Código Morse traducido: {texto}")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

if __name__ == "__main__":
    main()
