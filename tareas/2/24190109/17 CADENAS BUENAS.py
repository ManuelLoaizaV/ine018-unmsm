def Resultado(a):
    resultado = []
    
    for char in a:
        if resultado and resultado[-1].islower() and resultado[-1].upper() == char:
            resultado.pop()
        else:
            resultado.append(char)
    
    print("".join(resultado))


Resultado("UNMSM")  
Resultado("s")      
Resultado("xabBAycCz")  
Resultado("xaaabbbBBBAAAd") 
