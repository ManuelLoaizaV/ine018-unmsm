def invertir_cadena(s):
    return s[::-1]

def convertir_a_buena(s):
    caracteres = []
    for char in s:
        if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == char:
            caracteres.pop()
        else:
            caracteres.append(char)

    return invertir_cadena(''.join(caracteres))

if __name__ == "__main__":
    print(convertir_a_buena("UNMSM"))
    print(convertir_a_buena("sS"))
    print(convertir_a_buena("xaBBAyCcZ"))
    print(convertir_a_buena("xaaabbbBBBBAAAAd"))