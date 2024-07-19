#Demasiadas funciones para poder escribir correctamente en el archivo de salida
def comando_de_ayuda():

    return ("Ingrese expresiones en RPN,\n"
            "en donde los operadores aparecen luego de\n"
            "los operandos sobre los cuales serán aplicados.\n"
            "Cada línea consiste de número, un operador,\n"
            "o uno de los siguientes comandos:\n"
            "Q: Terminar el programa\n"
            "H: Mostrar este mensaje de ayuda\n"
            "C: Limpiar la memoria de la calculadora\n")

def es_operador(s):

    return s == '+' or s == '-' or s == '*' or s == '/'

def aplicar_operador(operador, memoria):

    ultimo = memoria.pop()
    penultimo = memoria.pop()

    if operador == "+":
        resultado = penultimo + ultimo
    elif operador == "-":
        resultado = penultimo - ultimo
    elif operador == "*":
        resultado = penultimo * ultimo
    elif operador == "/":
        resultado = penultimo / ultimo

    memoria.append(resultado)

    return resultado

def main():
    archivo_entrada = "entrada_ejercicio17.txt"
    archivo_salida = "salida_ejercicio17.txt"

    with open(archivo_entrada, encoding="utf-8") as entrada:
        entrada = entrada.readlines()
    with open(archivo_salida, 'w', encoding="utf-8") as salida:
            salida.write(comando_de_ayuda() + "\n\n")

            memoria = []
            #Lista vacía

            for linea in entrada:
                entrada = linea.strip()
                #Para eliminar espacios en blanco

                if entrada == "Q":
                    break

                elif entrada == "C":
                    memoria.clear()

                elif entrada == "H":
                    salida.write(comando_de_ayuda() + "\n\n")

                elif es_operador(entrada):
                    resultado = aplicar_operador(entrada, memoria)

                else:
                        memoria.append(float(entrada))

            salida.write(f"Resultado final: {memoria[-1]}\n")
            #Con los numeros negativos accedemos desde el ultimo indice de la lista
                    

if __name__ == "__main__":
    main()
