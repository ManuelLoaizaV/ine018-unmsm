with open('input.txt', 'r') as file:
  v = []
  for line in file:
    v.append(int(line.strip()))
    #line.strip elimina los \n

def HallarMedia(v):
  #v = [1,2,3,4,5,6,7,8,9,10]
  suma = 0
  for n in v:
    suma = suma + n
  promedio = suma/len(v)
  return promedio

with open('output.txt', 'w') as file:
  file.write(str(HallarMedia(v)))