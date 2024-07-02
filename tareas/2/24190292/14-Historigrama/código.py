valores_que_deseamos = input()
valores = valores_que_deseamos.split()
datos_ordenados= [int(val) for val in valores ]
historigrama = [0,0,0,0,0,0,0,0,0,0,0]
for bal in datos_ordenados:
    if 0<=bal<2: 
        historigrama[0]+=1
    if 2<=bal<4:
        historigrama[1]+=1
    if 4<=bal<6: 
        historigrama[2]+=1
    if 6<=bal<8:
        historigrama[3]+=1
    if 8<=bal<10: 
        historigrama[4]+=1
    if 10<=bal<12:
        historigrama[5]+=1
    if 12<=bal<14: 
        historigrama[6]+=1
    if 14<=bal<16:
        historigrama[7]+=1
    if 16<=bal<18: 
        historigrama[8]+=1
    if 18<=bal<20:
        historigrama[9]+=1
    if 20 == bal:
        historigrama[10]+=1
a=0
for dat in historigrama:
    print(a,": ",end=" ")
    for _ in range(dat):
        print("*",end=" ")
    print()    
    a+=2

