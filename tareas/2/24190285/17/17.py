def comando_de_ayuda():
    return "Ingrese expresiones en RPN,\n" \
           "en donde los operadores aparecen luego de\n" \
           "los operandos sobre los cuales seran aplicados.\n" \
           "Cada linea consiste de numero, un operador,\n" \
           "o uno de los siguientes comandos:\n" \
           "Q: Terminar el programa\n" \
           "H: Mostrar este mensaje de ayuda\n" \
           "C: Limpiar la memoria de la calculadora\n"

def es_operador(s):
    return s in ['+','-','*','/']

def aplicar_operador(operador,memoria):
    derecha=memoria.pop()
    izquierda=memoria.pop()
    if operador=='+':
        resultado=izquierda + derecha
    elif operador=='-':
        resultado=izquierda - derecha
    elif operador=='*':
        resultado=izquierda * derecha
    elif operador=='/':
        resultado=izquierda / derecha
    memoria.append(resultado)
    return str(resultado) + '\n'
#elif es la abreviación de else if
# append sirve para agregar un elemente al final de la lista

with open('17entrada.txt','r') as entrada:
    leer=entrada.read()

memoria=[]
resultados=[]
lineas_entrada=leer.splitlines()
#el splitlines sirve para dividir una cadena en una lista de líneas
for linea in lineas_entrada:  
    if linea=='Q':
        break
    elif linea=='C':
        memoria=[]
    elif linea=='H':
        resultados.append(comando_de_ayuda())
    elif es_operador(linea):
        resultados.append(aplicar_operador(linea, memoria))
    else:
        memoria.append(float(linea))

with open('17salida.txt', 'w') as salida:
    salida.writelines(resultados)




