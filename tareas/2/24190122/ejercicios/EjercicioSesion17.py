def invertir_cadena(s):
    return s[::-1]

def convertir_a_buena(s):
    caracteres = []
    for char in s:
        if caracteres and caracteres[-1].lower() == char.lower():
            caracteres.pop()
        else:
            caracteres.append(char)
    
    r = ''.join(caracteres)
    return invertir_cadena(r)

if __name__ == "__main__":
    print(convertir_a_buena("UNMSM"))
    print(convertir_a_buena("s"))
    print(convertir_a_buena("xabBAycCz"))
    print(convertir_a_buena("xaaabbbBBBAAAd"))