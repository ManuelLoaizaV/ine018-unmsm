# Pude leer que las variables adquieren su tipo en tiempo de ejecución según el valor que se les asigna,
# me resulta sorprendente que sea tan dinámico.
# Es genial que solo se definan con un "def".
def AplicarOperador(operador, lista):
# A diferencia de C++, Python permite el acceso a los elementos de una lista utilizando números negativos:
# -1 = último, -2 = penúltimo, etc.
# Creo que no era necesario porque, aquí, el pop elimina el resultado a la vez que te lo retorna, pero bueno.
        derecha = lista[-1]
        lista.pop()
        izquierda = lista[-1]
        lista.pop()
# else if = elif
        if operador == "+":
            resultado = izquierda + derecha
        elif operador == "-":
            resultado = izquierda - derecha
        elif operador == "/":
            resultado = izquierda / derecha
        elif operador == "*":
            resultado = izquierda * derecha

        lista.append(resultado)
        return resultado

# Vi que se podía hacer esto, así que lo utilicé para tener más orden y estar más seguro xd.

def main(): 

    with open('Reverse_polish_notation_entrada.txt', 'r') as entrada: 
        lineas = entrada.readlines() # Para leer todas las líneas.

    with open ('Reverse_polish_notation_salida.txt', 'w') as salida:
        mensaje = (
            ">" + "\n" + "Ingrese expresiones en RPN," + "\n" + 
            "en donde los operadores aparecen luego de" + "\n" +
            "los operandos sobre los cuales serán aplicados." + "\n" +
            "Cada línea consiste de número, un operador" + "\n" +
            "o uno de los siguientes comandos:" + "\n" +
            " Q: Terminar el programa" + "\n" +
            " H: Mostrar este mensaje de ayuda" + "\n" +
            " C: Limpiar la memoria de la calculadora" + "\n"
        )
        salida.write(">" + "\n" + "Simulación de calculadora RPN (ingrese H para ayuda)" + "\n")

        # Definimos lista vacía.
        memoria = []

        for linea in lineas:
            entrada = linea.strip() 
            # Supuestamente xd, elimina caracteres no deseados para que no hayan errores en el for.
        # Lo había hecho inicialmente con while (While True), pero no sabía si eso permitiría que 
        # fueran las líneas fueran reconocidas por el código.
            if entrada == "Q":
               break
            elif entrada == "H":
                salida.write(mensaje)
            elif entrada == "C":
                memoria.clear()
                salida.write(">" + "\n" + "Memoria completamente limpia :)" + "\n" + ">" + "\n")
            elif entrada in ["+", "-", "*", "/"]: # Esto es muy práctico.
                resultado = AplicarOperador(entrada, memoria)
                salida.write(str(resultado) + "\n")
            else:
                memoria.append(float(entrada))
# Convención común en Python que se utiliza para asegurarse de que el código en este bloque se 
# ejecute solo cuando el script se ejecuta directamente y no cuando se importa como un módulo en otro script.
# Sinceramente, siento que podría entender mejor el concepto xd, pero lo dejé aquí por temor a que altere
# algo importante y luego no funcione mi main.
if __name__ == "__main__":
    main()