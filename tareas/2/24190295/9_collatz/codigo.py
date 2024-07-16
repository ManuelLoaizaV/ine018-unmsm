m = int(input())

while m > 1:
    if m % 2 != 0:
        #verifico que es impar
        print(f"{m}  3m+1 : {3 * m+1}")
        m = m * 3 + 1
        
    else:
        #aqui sera par 
     print(f"{m} mitad {m//2}")
     m = m//2
