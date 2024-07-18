def main():
    n = 27
    pasos = 0
    original = n

    while (n>1):
        m = 0
        if n % 2 == 0:
            m = n/2
            print(f'{n} es par, entonces tomo la mitad: {m}')
        else:
            m = 3*n + 1
            print(f'{n} es impar, entonces hago 3n + 1: {m}')
        n = m
        pasos+=1
    
    print(f'Wow fue un viaje de {pasos} paso(s) desde {original} hasta 1')
    print(f'Pero al final llegue. Eso quiere decir que {original} es maravilloso')
    print(f'Me pregunto que numeros no seran maravillosos')

main()
