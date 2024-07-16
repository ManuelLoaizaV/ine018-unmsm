def convertirAbuena(s):
    stack=[]
    for char in s:
        if stack and stack[-1].islower() and stack[-1].upper() == char:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

cadena= input("Ingrese cadena: ")

resultado = convertirAbuena(cadena)

print( resultado)