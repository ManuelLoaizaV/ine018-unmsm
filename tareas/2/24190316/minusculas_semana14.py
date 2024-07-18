def minusculas(frase):
    nueva_frase = ""
    for letra in frase:
        if ('A' <= letra) and (letra <= 'Z'):
            letra = (ord(letra) - ord('A')) + ord('a')
            letra = chr(letra)
        nueva_frase = f'{nueva_frase}{letra}'
    return nueva_frase

print(minusculas("ThECAKeISALiE"))