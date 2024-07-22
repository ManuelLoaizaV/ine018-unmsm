def cadena_a_entero(s):
  n=len(s)
  entero=0
  inicio=0
  if s[0]=='-':
      inicio=1
  for i in range(inicio, n):
      entero=10*entero+(ord(s[i])-ord('0'))
  if s[0]=='-':
      entero*=-1
  return entero
def main():
  print(cadena_a_entero("28"))
  print(cadena_a_entero("-496"))
  print(cadena_a_entero("0"))
  print(cadena_a_entero("8128"))
  print(cadena_a_entero("-33550336"))
  a="-12"
  b="34"
  c=cadena_a_entero(a) + cadena_a_entero(b)
  print(c)
if __name__ == "__main__":
  main()