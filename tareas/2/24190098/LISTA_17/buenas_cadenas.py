def InvertirCadena(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r

def ConvertirABuena(s):
    b = []
    for char in s:
        if b and b[-1].islower() and b[-1].upper() == char:
            b.pop()
        else:
            b.append(char)
    
    r = ""
    while b:
        r += b.pop()
    
    return InvertirCadena(r)

s = input("Ingrese una cadena: ")
resultado = ConvertirABuena(s)
print(resultado)
