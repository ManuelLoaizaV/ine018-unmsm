def invertir_cadena(s):
  return s[::-1]
def convertir_a_buena(s):
  caracteres=[]
  for char in s:
      if caracteres and caracteres[-1].islower() and caracteres[-1].upper()==char:
        caracteres.pop()
      else:
        caracteres.append(char)
  return "".join(caracteres)
def main():
  print(convertir_a_buena("UNMSM"))
  print(convertir_a_buena("s"))
  print(convertir_a_buena("xabBAycCz"))
  print(convertir_a_buena("xaaabbbBBBAAAd"))
if __name__=="__main__":
  main()