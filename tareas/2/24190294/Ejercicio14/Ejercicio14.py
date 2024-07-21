def Mayusculas(s):
    cadena_mayusculas = ""
    for c in s:
        if 'a' <= c <= 'z':
            letra_mayuscula = chr(ord(c) - 32)
        else:
            letra_mayuscula = c
        cadena_mayusculas += letra_mayuscula
    return cadena_mayusculas

s = str(input())

palabra_mayuscula = Mayusculas(s)
print("Cadena en mayúsculas:", palabra_mayuscula)
