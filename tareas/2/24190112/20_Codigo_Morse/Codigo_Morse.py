#Declaramos los valores de letras a morse en un diccionario que seria como el equivalente a un mapa
letra_a_morse = {
        'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".",
        'F': "..-.",   'G': "--.",    'H': "....",   'I': "..",     'J': ".---",
        'K': "-.-",    'L': ".-..",   'M': "--",     'N': "-.",     'O': "---",
        'P': ".--.",   'Q': "--.-",   'R': ".-.",    'S': "...",    'T': "-",
        'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",   'Y': "-.--",
        'Z': "--.."
    }

#Esto si lo hice igual a usted profe
def En_morse(texto):
    for c in texto:
        if c == ' ':
            continue
        if c.isalpha():
            return False
    return True

#Si hay un espacio no haremos nada, y hacemos que el texto este en mayusculas para que coincida con el diccionario
def Texto_a_morse(texto):

    morse_texto = []
    texto_correcto = texto.upper()
    for c in texto_correcto:
        if c == ' ':
            continue
        if c in letra_a_morse:
            morse_texto.append(letra_a_morse[c])
    
    return ' '.join(morse_texto)
#El join es para unir las partes en una sola cadena separandola por un valor que en este casos seria un espacio en blanco

def Morse_a_texto(morse):
    morse_a_letra = {}
    #Diccionario vacio

    #Invertimos el diccionario de letra_a_morse
    for letra, codigo in letra_a_morse.items():
        morse_a_letra[codigo] = letra

    texto = []
    #Lista vacia
    codigos = morse.strip().split(' ')
    #Eliminamos los espacios en blanco y el split es para separar las subcadenas con espacios

    #Ahora si convertimos a texto luego de separar el codigo
    for codigo in codigos:
        if codigo in morse_a_letra:
            texto.append(morse_a_letra[codigo])
            #Añadimos a la lista luego de verificar si el codigo es de una letra
    
    return ''.join(texto)
#Finalmente uniremos a los caracteres dados sin espacios en blanco, todo junto ''

def main():
    archivo_entrada = "entrada_ejercicio20.txt"
    archivo_salida = "salida_ejercicio20.txt"

    with open(archivo_entrada, encoding = "utf - 8") as entrada:
        lineas = entrada.readlines()
        resultados = []

    #Ambos for son para que evalue cuantas lineas se pueda, aunque pude haber puesto manualmente me parece que esto
    # es más efectivo para un programa más trabajable    
    for linea in lineas:
        linea = linea.strip()
        if En_morse(linea):
            texto_convertido = Morse_a_texto(linea)
            resultados.append(f"Código morse a letras: {texto_convertido}")
        else:
            morse_convertido = Texto_a_morse(linea)
            resultados.append(f"Letra a código Morse: {morse_convertido}")
    
    with open(archivo_salida, 'w', encoding="utf-8") as salida:
        for resultado in resultados:
            salida.write(resultado + "\n")

if __name__ == "__main__":
    main()
