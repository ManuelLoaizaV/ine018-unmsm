entrada = input ("Ingrese una cadena: ")
caracteres = []
    
for char in entrada:
    if caracteres and caracteres[-1].lower() == char.lower() and caracteres[-1] != char:
        caracteres.pop()
    else:
        caracteres.append(char)
resultado = ''.join(caracteres)
print (resultado)