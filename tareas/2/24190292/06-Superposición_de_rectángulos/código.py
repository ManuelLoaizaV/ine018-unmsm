def main():
    
    def superponenrectángulos(a,b,alto_1,ancho_1,x,y,alto_2,ancho_2):
        if y > b + alto_1 or b > y + alto_2:
            return False
        if a + ancho_1 < x or x + ancho_2 < a:
            return False
        if a < x and x + ancho_2 < a + ancho_1 and y + alto_2 < b + alto_1 and b < y:
            return False
        if a > x and x + ancho_2 > a + ancho_1 and y + alto_2 > b + alto_1 and b > y:
            return False
        return True
    
    if superponenrectángulos(-3,-2,3,4,-5,2,3,3):
        print("verdad")
    else:
        print("falso")
    
    
if __name__ == "__main__":
    main()
