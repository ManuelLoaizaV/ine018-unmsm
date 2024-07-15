import math

def main():
    a = float(input("Ingrese el valor del primer cateto: "))
    b = float(input("Ingrese el valor del segundo cateto: "))
    c = math.sqrt(a * a + b * b)
    print(f"Por el teorema de Pitagoras, la hipotenusa mide {c}")

if __name__ == "__main__":
    main()
