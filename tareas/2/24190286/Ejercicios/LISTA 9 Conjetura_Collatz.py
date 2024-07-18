a= int(input())

while a != 1:
    if a%2==0:
        print(f"{a} es par, entonces tomo la mitad: {a//2}")
        a=a//2
    else:
        
        print(f"{a} es impar, entonces hago 3n+1 : {3*a+1}")
        a=a*3+1
           
    