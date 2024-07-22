from sympy import symbols, Matrix, solve
def cumpleConL(L,A):
    if len(solve(L - A, t )) > 0 :
        return True
    else:
        return False 

t= symbols('t', real=True)
L = Matrix([4,4,4])+Matrix([3,4,1])*t
A = Matrix([2,1,-4])
B = Matrix([7,8,5])
C = L


if cumpleConL(L,A) and not cumpleConL(L,B):

    #si A pertenece y B No : C Pertenence y existe solución si AB = BC
    Condicion = (B-A).norm() - (Matrix([4,4,4])+Matrix([3,4,1])*t-B).norm()
    Eq = solve(Condicion, t)
    if  len(Eq) >0 :
        descartamos = solve(L-A,t)
        if descartamos in Eq:
            Eq.remove(descartamos)
        #solo queda un valor para Eq
        C = L.subs(t, Eq[0]) 
        M= (A+C)/2
        print("las coordenadas del punto medio de las bases son:",M)
    else: 
        print("no existe solución")

elif not cumpleConL(L,A) and  cumpleConL(L,B):

    #si B pertenece y A No : C Pertenence y existe solución si AB = AC
    Condicion = (B-A).norm() - (Matrix([4,4,4])+Matrix([3,4,1])*t-A).norm()
    Eq= solve(Condicion, t)

    #como sabemos que puede haber dos valores para t pues dan B y C que cumplen 
    #, eliminamos cuando t es el valor en B

    descartamos = solve(L-B,t)
    if descartamos in Eq:
        Eq.remove(descartamos)

    #solo queda un valor para Eq
    C = L.subs(t, Eq[0]) 
    M= (B+C)/2
    print("las coordenadas del punto medio de las bases son:",M)
    
else:
    # si A Pertence y B tmb: C no pertence existen infinitos 
    print("En C no existe única solución gaa")