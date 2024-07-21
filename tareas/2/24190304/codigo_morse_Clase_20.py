letra_a_morse = {
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..',
    }
#para poder traducir de código Morse a letras
MorseaLetras = {codigo: letra for letra, codigo in letra_a_morse.items()}

def EsMorse(texto):
    return all(c == ' ' or not c.isalpha() for c in texto)

def main():
    
    print("Traductor de código Morse")

#Fue en el que más se me hizo muy complicado, pero al final lo logré
#Al final me di cuenta que casi es la misma estructura del c++ solo que se cambian algunos codigos

    while True:
        entrada = input("> ")
        if entrada.lower() == "salir":
            break
        print(traductor(entrada))
        
#
def traductor(texto):
    traduccion = ""
    if EsMorse(texto):
        palabras_morse = texto.split()
        
        for palabra in palabras_morse:
            if palabra in MorseaLetras:
                traduccion += MorseaLetras[palabra]
    else:
        
        for char in texto:
            if char.upper() in letra_a_morse:
                traduccion += letra_a_morse[char.upper()] + " "
    return traduccion.strip()

if __name__ == "__main__":
    main()