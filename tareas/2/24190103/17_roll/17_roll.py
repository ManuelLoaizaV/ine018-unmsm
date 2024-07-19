with open('input.txt', 'r') as file:
  value = file.readline().split()
  value1 = file.readline().split()
  value2 = file.readline().split()

  x = int(value[0])
  y = int(value[1])

  x1 = int(value1[0])
  y1 = int(value1[1])

  x2 = int(value2[0])
  y2 = int(value2[1])

def Roll(fila, n, k):
  fila = ['A', 'B', 'C', 'D']
  fila_to_roll = fila[-n:]
  fila_fija = fila[:(4-n)]

  #Def k_veces
  rolled = fila_to_roll
  for i in range(k):
    rolled = [rolled[-1]] + rolled[:-1]
  
  return ''.join(fila_fija + rolled)

fila = ['A', 'B', 'C', 'D']

with open('output.txt', 'w') as file:
  file.write(Roll(fila, x, y) + '\n')
  file.write(Roll(fila, x1, y1) + '\n')
  file.write(Roll(fila, x2, y2) + '\n')