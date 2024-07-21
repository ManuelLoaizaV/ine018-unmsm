Mor_letters= {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.",'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N':"-", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."}
Mor_letters_Invertido = {valor:llave for llave,valor in Mor_letters.items()}
#Me confudio  al inico pero sirvio para invertilos llave por llave,y entendi uu.

def Encriptar(cadena):
    ABC= []
    for char in cadena.upper():
        if char in Mor_letters:
           ABC.append(Mor_letters[char])
    Encripty =''.join(ABC)
    return Encripty

#Me confundio un poco usar join,ya que no sabia si me devolveria los `A` o los .-..

def Lectura(cadena):
    Leer = []
    new_cadena = cadena.split(' ') 
    for char in new_cadena:
        if char in Mor_letters_Invertido:
            Leer.append(Mor_letters_Invertido[char])
    Lectuty =' '.join(Leer)
    return Lectuty

#Me sorprende lo rapido que puede ser manejar listas con join y split.      

while True : 
    cadena = input("Ingrese texto o codigo Morse (enter para salir): ")
    
    if cadena == "":
        break
    elif cadena[0].isalpha():
        Resultado_Morse = Encriptar(cadena)
        print(f"Convertido a Morse: {Resultado_Morse}")
    elif cadena[0] in ['.', '-']:
        Resultado_Texto = Lectura(cadena)
        print(f"Cconvertido a texto: {Resultado_Texto}")
    else:
        print("Entrada no valida.")
#No se como hacer para que identifique una palabra, se detenga y un espacio.
#Es complicado :c.