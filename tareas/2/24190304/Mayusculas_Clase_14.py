def ConvertirenMayuscula(s):
  
  Modificado = []
  
  for char in s:
    
    #Verifico que la cadena este en el rago de a hasta la z
      if 'a' <= char <= 'z':
    
    #Logre encontrar estos codigos ord toma el char y devuelve un ASCII 
    #chr lo convierte a un caracter denuevo
          char = chr(ord(char) - ord('a') + ord('A'))
      
      Modificado.append(char)

  return ''.join(Modificado)

print(ConvertirenMayuscula("Manuel Loaiza"))       
print(ConvertirenMayuscula("alex cisneros")) 
print(ConvertirenMayuscula("ARIADNA ROSSA")) 
print(ConvertirenMayuscula("pi=3.1415926535897932")) 
s = "UnMsm2024"
print(ConvertirenMayuscula(s))        