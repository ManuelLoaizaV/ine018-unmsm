#ejercicio_sesión_9
hermoso = int(input())
trayecto = 0

while(hermoso != 1):
    inicio = 0
    if(hermoso%2 == 0):
            inicio = hermoso/2
            trayecto += 1
            caso1 = f"{int(hermoso)} es par, entonces tomo la mitad: {int(inicio)}"
            print(caso1)
    else:
            inicio = 3*hermoso + 1
            trayecto += 1
            caso2 = f"{int(hermoso)} es impar, entonces hago 3n + 1: {int(inicio)}"
            print(caso2)
    hermoso = inicio
        
total = f"{trayecto} pasos"
print(total)
