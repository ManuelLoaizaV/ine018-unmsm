import string

def imprimir_frecuencias(s):
    frecuencias = {letter: 0 
                   for letter in string.ascii_lowercase
                   }
    for c in s.lower():
        if c in frecuencias:
            frecuencias[c] = frecuencias[c] + 1
    print(s)
    for letra in sorted(frecuencias):
        if frecuencias[letra]>0:
            print(letra , "=", frecuencias[letra])
    print()

imprimir_frecuencias("Miguel")
imprimir_frecuencias("alejandro")
imprimir_frecuencias("UNMSM")