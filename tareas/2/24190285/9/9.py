with open('9entrada.txt', 'r') as entrada:
    num = int(entrada.readline())  #se lee el número qu se encuentra en el txt de entrada

    with open('9salida.txt', 'w') as salida:
        while num != 1:
            if num % 2 == 0:
                num3 = num // 2
                salida.write(f"{num} es par entonces tomo la mitad: {num3}\n")
            else:
                num3 = 3 * num + 1
                salida.write(f"{num} es impar entonces hago 3n+1: {num3}\n")
#como son 2 casos(para números pares e impares)son 2 tipos de salidas, se sigue ejecutando hasta que llegue a 1
            num = num3 

        
