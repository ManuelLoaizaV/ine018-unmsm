def convertirBuena(frase):
    nueva_frase = frase
    for tamaño in range(len(frase)-1):
        letra = frase[tamaño]
        letra_siguiente = frase[tamaño+1]
        if letra.islower() and letra_siguiente.isupper():
            nueva_frase = nueva_frase.replace(letra, '', 1)
            nueva_frase = nueva_frase.replace(letra_siguiente, '', 1)
    
    return nueva_frase

def EsBuena(frase):
    for tamaño in range(len(frase)-1):
        letra = frase[tamaño]
        letra_siguiente = frase[tamaño+1]
        if letra.islower() and letra_siguiente.isupper():
            return False
    return True

frase = "xaaabbbBBBAAAd"
while not EsBuena(frase):
    frase = convertirBuena(frase)
print(frase)
