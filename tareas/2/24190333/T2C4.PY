def minusculas(s):
    resultado = ""
    for char in s:
        if 'A' <= char <= 'Z':
            resultado += chr(ord(char) - ord('A') + ord('a'))
        else:
            resultado += char
    return resultado
palabra= (input("Ingresar palabra u oración:"))
print(minusculas(palabra))