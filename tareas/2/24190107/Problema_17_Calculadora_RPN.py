def Comando_de_Ayuda():
    print("Ingrese expresiones en RPN,")
    print("en donde los operadores aparecen luego de")
    print("los operandos sobre los cuales serán aplicados.")
    print("Cada línea consiste de número,un operador,")
    print("o uno de los siguientes comandos:")
    print("Q: Terminar el programa")
    print("H: Mostrar este mensaje de ayuda")
    print("C: Limpiar la memoria de la calculadora")

def Operador(signo):
    return signo in ['+','-','*','/']

def Llamada(signo, dato):
    derecha = dato.pop()
    izquierda = dato.pop()
    if signo== '+':
        resultado = izquierda + derecha
    elif signo == '-':
        resultado= izquierda - derecha
    elif signo == '*':
        resultado= izquierda * derecha
    elif signo== '/':
        resultado = izquierda / derecha
    print(resultado)
    dato.append(resultado)

#me confundi con el .pop tiene otra funcion mas(de devolver el valor).
print("Simulación de calculadora RPN (ingrese H para ayuda)")

dato = []
while True:
    entrada = input()
    if entrada == 'Q':
        break
    elif entrada == 'C' :
        dato.clear()
    elif entrada == 'H':
        Comando_de_Ayuda()
    elif  Operador(entrada):
        Llamada(entrada , dato)
    else:
        dato.append(float(entrada))
