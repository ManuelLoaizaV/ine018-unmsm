def ConvertirABuena(a):
    lista=[]
    for char in a:
        if lista and lista[-1].islower() and lista[-1].upper() == char:
            lista.pop()
        else:
            lista.append(char)
    #esto es algo que me sorprendio(volver una lista en string con un solo paso)
    r = "".join(lista)
    print(r)

ConvertirABuena("UNMSM") 
ConvertirABuena("s") 
ConvertirABuena("xabBAycCz") 
ConvertirABuena("xaaabbbBBBAAAd") 