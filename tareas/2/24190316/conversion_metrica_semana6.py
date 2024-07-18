def main():
    print("Ingrese la cantidad en metros: ")
    metros = float(input())

    pulgadas = metros / 0.0254
    pies = metros / 12

    print(f'Distancia en pulgadas {pulgadas}')
    print(f'Distancia en pies {pies}')
    
main()