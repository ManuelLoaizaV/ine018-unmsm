with open('input.txt', 'r') as file:
    pulgadas = int(file.readline().strip())
    pulgadas1 = int(file.readline().strip())
    pulgadas2 = int(file.readline().strip())

def ExcesoDeTela(pulgadas):
    n = 0
    while n*36 - pulgadas < 0:
        n += 1
    return n*36 - pulgadas

with open('output.txt', 'w') as file:
    file.write(str(ExcesoDeTela(pulgadas))+ '\n')
    file.write(str(ExcesoDeTela(pulgadas1)) + '\n')
    file.write(str(ExcesoDeTela(pulgadas2)) + '\n')