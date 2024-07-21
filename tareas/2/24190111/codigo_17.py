def main():
    with open('17_entrada.txt','r') as entrada:
        s = entrada.readline()

    caracteres = []
    for char in s:
        if caracteres and caracteres[-1].lower() ==char.lower() and caracteres[-1]!= char:
            caracteres.pop()
        else:
            caracteres.append(char)

    resultado = ''.join(caracteres)
    with open('17_salida.txt','w') as salida:
        salida.write("La nueva cadena es: " +resultado)

if __name__ =="__main__":
    main()
