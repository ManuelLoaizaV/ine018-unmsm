def suma_primeros_impares(N):
    suma = 0
    
    for i in range(N):
        numero_impar = 2*i + 1
        suma += numero_impar
    
    return suma

N = int(input("Ingrese un número entero positivo: "))
resultado = suma_primeros_impares(N)
print(f"La suma de los primeros {N} números impares es: {resultado}")
