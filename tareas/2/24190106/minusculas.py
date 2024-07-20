def convertir_minu(s1):
    c_result = []#mantendo la cadena vacía
    
    for char in s1:#ord y chr devuelve el numero ascci y el caracter respectivamente
        if 'A' <= char <= 'Z':
            s2 = chr(ord(char) + 32)
        else :
            s2 = char
        c_result.append(s2)#agrego los valores al final de mi cadena
    return ''.join(c_result)

s = input()
s_en_minu = convertir_minu(s)
print (s_en_minu)
