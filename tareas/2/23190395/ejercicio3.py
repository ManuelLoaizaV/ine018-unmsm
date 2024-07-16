def Minusculas(s):
    # Convertimos la cadena a minúsculas usando el método lower()
    return s.lower()

def main():
    s = input("Ingrese una cadena: ")
    resultado = Minusculas(s)
    print(resultado)

if __name__ == "__main__":
    main()
