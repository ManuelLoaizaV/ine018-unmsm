with open('input.txt', 'r') as file:
  term1 = file.readline().strip() #sin el .strip() no funcionaba
  term2 = file.readline().strip()
  term3 = file.readline().strip()
  term4 = file.readline().strip()

def get_key(val):
  keys = []
  for key, value in diccionario.items():
        if val in value:
          keys.append(key)
            #return key
  if keys:
    #return keys
    return '\n'.join(keys)
  else:
    return "El código postal no existe."

def exist(diccionario, term):
  
  if diccionario.get(term):
    #return(diccionario.get(term))
    return '\n'.join(diccionario.get(term))
  else:
    return("El distrito no existe.")

diccionario = {
    'Europa': ['España', 'Francia', 'Inglaterra'],
    'Sudamerica': ['Peru', 'Chile', 'Francia', 'Argentina'],
    'Breña' : ['15082', '15083'],
    'Magdalena del Mar' : ['7021', '15076', '15086'],
    'San Miguel' : ['15086', '15087', '15088'],
    'Pueblo Libre' : ['15083', '15084', '15086', '15088'],
    'Jesus María' : ['2002', '15072', '15073', '15076', '15084'],
    'Lima' : ['17006', '15001', '15003', '15004', '15006', '15018', '15046', '15079', '15081', '15082', '15083', '15085', '15088', '15093', '15101', '15822', '21001']
}

with open('output.txt', 'w') as file:
  file.write(str(exist(diccionario, term1)) + '\n')
  file.write(str(exist(diccionario, term2)) + '\n')
  file.write(str(get_key(term3)) + '\n')
  file.write(str(get_key(term4)) + '\n')