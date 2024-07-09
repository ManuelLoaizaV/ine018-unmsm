# Ahora son '#' para los comentarios... ojo

with open('Suma_de_numeros_impares_entrada.txt', 'r') as entrada:
    num = int(entrada.readline()) 
    num1 = int(entrada.readline()) 
    #Yo que pensé que escapaba de las especificaciones de variables :,
    #Aquí especifico el 'int', porque sino se lee como 'str' y necesito trabajarlo como un número

resultado = num*num
final_de_suma = 2* num - 1 

resultado1 = num1*num1
final_de_suma1 = 2* num1 - 1 

with open('Suma_de_numeros_impares_salida.txt', 'w') as imprimo:
    imprimo.write("La suma de 1 + ... + " + str(final_de_suma) + " es " + str(resultado) + "\n" +
                  "La suma de 1 + ... + " + str(final_de_suma1) + " es " + str(resultado1))
#Solo se imprimen 'str' por lo que tengo que transformar mis números a str e.e