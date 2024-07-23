with open('entrada.txt','r') as archivo:
  n=int(archivo.read())
pasos= 0
original = n

with open('salida.txt','w') as archivo2:
  while n>1:

    if n%2==0:
      m=n/2
      archivo2.write(f"{int(n)} es par, estonces tomo la mitad: {int(m)}\n")

    else:
     m=3*n+1
     archivo2.write(f"{int(n)} es impar, entonces hago 3n + 1: {int(m)}\n")
    n=m
    pasos=pasos +1

archivo2.write(f"Wow, fue un viaje de {pasos} paso(s) desde {original} hasta 1.")
archivo2.write(f"Pero al final llegué. Eso quiere decir que {original} es maravilloso.")
archivo2.write("Me pregunto qué números no serán maravillosos ...")
