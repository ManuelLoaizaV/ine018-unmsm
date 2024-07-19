with open('14entrada.txt', 'r') as entrada:
    s=entrada.read()
#se lee el txt
def mayusculas(s):
    return s.upper()
 #se convierte todo el texto a mayúscula   
with open('14salida.txt', 'w') as salida:
     salida.write(mayusculas(s))   
