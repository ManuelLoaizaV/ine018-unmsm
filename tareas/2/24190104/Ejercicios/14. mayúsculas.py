nombre = input()

nombre_mayusculas = ""

for char in nombre:
    if 'a' <= char <= 'z':
        # Convertimos el carácter a mayúsculas restando 32 de su valor ASCII
        nombre_mayusculas += chr(ord(char) - 32)
    else:
        # Añadimos la letra
        nombre_mayusculas += char

print(nombre_mayusculas)





