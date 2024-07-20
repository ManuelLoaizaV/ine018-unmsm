def InvertirCadena(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r

def ConvertirABuena(s):
    caracteres = []
    for char in s:
        if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == char:
            caracteres.pop()
        else:
            caracteres.append(char)
    
    r = ""
    while caracteres:
        r += caracteres.pop()
    
    return InvertirCadena(r)

def main():
    s = input("Ingrese una cadena: ")
    resultado = ConvertirABuena(s)
    print(resultado)

if __name__ == "__main__":
    main()
