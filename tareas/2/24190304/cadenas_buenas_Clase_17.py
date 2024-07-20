def ConvertirACadenaBuena(s):
# Profesorrrrrrr en esta si me complique mucho :( 
    Cadena = []
 
    for char in s:
# Encontre estos codigos que me ayudaron mucho Lower lo utilizo para convertir a minúsculas y el upper para mayúsculas

# El isupper para ver si es mayuscula y el islower para ver si es minuscula
    
    #En c++ se utilizaba el back para encontrar el último elemento de la lista, 
    #Tuve que buscar con que reemplazarlo  y encontre esto Cadena[-1]
        
        if Cadena and ((Cadena[-1] == char.lower() and char.isupper()) or 
                       
                       (Cadena[-1] == char.upper() and char.islower())):

# Si forman un par problemático, eliminamos el carácter de la cima de la pila
            Cadena.pop()
        else:

# Si no forman un par problemático, agregamos el carácter actual a la pila
            Cadena.append(char)

 
    return ''.join(Cadena)


t = "xabBAycCz"
print(ConvertirACadenaBuena(t))  
s = "fajsjaJjaSs"
print(ConvertirACadenaBuena(s)) 
print(ConvertirACadenaBuena("UNMSM"))           
print(ConvertirACadenaBuena("xabBAycCz"))       
print(ConvertirACadenaBuena("xaaabbbBBBAAAd"))  