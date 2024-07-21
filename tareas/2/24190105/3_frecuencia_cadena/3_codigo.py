def ImprimirFrecuencias(s):
    frecuencias = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for c in s:
        if 'A' <= c <= 'Z':
            c = c.lower()
     
        if 'a' <= c <= 'z':
            frecuencias[c] += 1

    with open('3_salida.txt', 'w') as salida: 
        for letra, frecuencia in frecuencias.items():
            if frecuencia > 0:
               salida.write(f"{letra} = {frecuencia}\n")

with open ('3_entrada.txt', 'r') as entrada:
  s = str(entrada.readline()) 

ImprimirFrecuencias(s)
