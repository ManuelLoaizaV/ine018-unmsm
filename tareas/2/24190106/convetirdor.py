def convertir(celsius):
    return (celsius*9/5) + 32

celsius = float(input())
fahrenheit = convertir(celsius)
print(fahrenheit)