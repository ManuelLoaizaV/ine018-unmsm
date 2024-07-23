from collections import deque

def convertir_a_buena(s):
    caracteres = deque()
    for c in s:
        if caracteres and caracteres[-1].islower() and caracteres[-1].upper() == c:
            caracteres.pop()
        else:
            caracteres.append(c)
    return ''.join(caracteres)

print(convertir_a_buena("UNMSM"))
print(convertir_a_buena("s"))
print(convertir_a_buena("xabBAycCz"))
print(convertir_a_buena("xaaabbbBBBAAAd"))