def Cadena_nueva():
    m = input()
    c = []
    b = 0
    
    while b < len(m):
        if c and c[-1].islower() and c[-1].upper() == m[b]:
            c.pop() 
        else:
            c.append(m[b])  
        
        b += 1
    
    return ''.join(c)

print(Cadena_nueva())
