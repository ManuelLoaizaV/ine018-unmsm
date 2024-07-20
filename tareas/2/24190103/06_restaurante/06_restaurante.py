with open('input.txt', 'r') as file:
  costo_plato = int(file.read())
  
propina = costo_plato * 0.1
impuesto = costo_plato * 0.08
total = costo_plato + propina + impuesto

with open('output.txt', 'w') as file:
  file.write(str(impuesto) + '\n') 
  file.write(str(propina) + '\n')
  file.write(str(total) + '\n')