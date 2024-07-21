import sys

def comando_de_ayuda():
    print("Ingrese expresiones en RPN,")
    print("en donde los operadores aparecen luego de")
    print("los operandos sobre los cuales serán aplicados.")
    print("Cada línea consiste de número, un operador,")
    print("o uno de los siguientes comandos:")
    print("Q: Terminar el programa")
    print("H: Mostrar este mensaje de ayuda")
    print("C: Limpiar la memoria de la calculadora")

def es_operador(s):
    return s in ['+', '-', '*', '/']

def aplicar_operador(operador, memoria):
    derecha = memoria.pop()
    izquierda = memoria.pop()
    if operador == '+':
        resultado = izquierda + derecha
    elif operador == '-':
        resultado = izquierda - derecha
    elif operador == '*':
        resultado = izquierda * derecha
    elif operador == '/':
        resultado = izquierda / derecha
    print(resultado)
    memoria.append(resultado)

if __name__ == "__main__":
    print("Simulación de calculadora RPN (ingrese H para ayuda)")
    memoria = []
    while True:
        entrada = input().strip()
        if entrada == 'Q':
            break
        elif entrada == 'C':
            memoria = []
        elif entrada == 'H':
            comando_de_ayuda()
        elif es_operador(entrada):
            try:
                aplicar_operador(entrada, memoria)
            except IndexError:
                print("Error: no hay suficientes operandos en la pila.")
                sys.exit(1)
        else:
            try:
                memoria.append(float(entrada))
            except ValueError:
                print("Error: entrada inválida.")
                sys.exit(1)