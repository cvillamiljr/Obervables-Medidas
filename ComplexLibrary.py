import math
def complexSum(a,b):
    real=a[0]+b[0]
    comple=a[1]+b[1]
    
    return real,comple
def complexRest(a,b):
    real=a[0]-b[0]
    comple=a[1]-b[1]
    
    return real,comple

def complexProduct(a,b):
    real=(a[0]*b[0])-(a[1]*b[1])
    comple=(a[0]*b[1])+(a[1]*b[0])
    
    return real,comple 
def complexDiv(a,b):
    real=((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    comple=((a[1]*b[0])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))

    return real,comple

def complexMod(a):
    mod=((a[0]**2)+(a[1]**2))**1/2

    return mod
def complexConj(a):
    entera=a[0]
    comple=-a[1]

    return entera,comple

def polarCartesiano(a):
    #Los angulos estan en grados
    r = a[0]
    ang = radGrados(a[1])
    v1 = r*(math.cos(ang))
    v2 = r*(math.sin(ang))
    return (v1,v2)

def cartesianoPolar(a):
    v1 = (a[0]**2 + a[1]**2)**(1/2)
    v2 = gradRadi(math.atan2(a[1],abs(a[0])))
    return(v1,v2)

def complexArg(a):
    v1 = math.atan2(a[1],a[0])
    return v1

def radGrados(num):
    return (num/180)*math.pi

def gradRadi(num):
    return (num*180)/math.pi


def adicionVectores(a,b):
    ans=[0*len(a) for n in range(len(a))]
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            ans[i] = complexSum(a[i],b[i])
        return ans

def restaVectores(a,b):
    ans=[0*len(a) for n in range(len(a))]
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            ans[i] = complexRest(a[i],b[i])
        return ans
def inversaVector(a):
    ans=[0*len(a) for n in range(len(a))]
    for i in range(len(a)):
        ans[i] = (-1*(a[i][0]),-1*(a[i][1]))
    return ans

def escalarXComplejo(e,v):
    ans=[[0]*len(v) for n in range(len(v))]
    for i in range(len(v)):
        real=e*v[i][0]
        complejo=e*v[i][1]
        ans[i]=(real,complejo)
    return ans
def sumaMatrices(a,b):
    ans=[[0]*len(a) for n in range(len(a))]
    if(len(a)!=len(b) and len(a[0])==len(b[0])):
        return "Las dimensiones de las matrices no son iguales"
    else:
        for i in range(len(a)):
            for j in range(len(a[i])):
                ans[i][j]=complexSum(a[i][j],b[i][j])
    return ans

def restaMatrices(a,b):
    ans=[[0]*len(a) for n in range(len(a))]
    if(len(a)!=len(b) and len(a[0])==len(b[0])):
        return "Las dimensiones de las matrices no son iguales"
    else:
        for i in range(len(a)):
            for j in range(len(a[i])):
                ans[i][j]=complexRest(a[i][j],b[i][j])
    return ans
    
def inversaMatriz(a):
    ans=[[0]*len(a) for n in range(len(a))]
    for i in range(len(a)):
        ans[i] = inversaVector(a[i])
    return ans

def escalarXMatriz(e,a):
    ans=[[0]*len(a) for n in range(len(a))]  
    for i in range(len(a)):
        ans[i]=escalarXComplejo(e,a[i])        
    return ans

def transpuestaMatriz(a):
    ans=[[0]*len(a) for n in range(len(a[0]))]
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans[j][i]=a[i][j]
    return ans

def conjugadoMatriz(a):
    ans=[[0]*len(a[0]) for n in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans[i][j]=complexConj(a[i][j])
    return ans

def dagaMatriz(a):
    ans=transpuestaMatriz(a)
    ans=conjugadoMatriz(ans)
    return ans

def matrixProduct(a,b):
    ans=[[0]*len(b[0]) for n in range(len(a))]

    
    if(len(a[0])!=len(b)):
        return "No se pueden multiplicar estas matrices"
    else:
        r=transpuestaMatriz(b)

        for i in range(len(a)):
            for j in range(len(r)):
                temp=(0,0)
                m=(0,0)
                for k in range(len(a[0])):
                    temp=complexProduct(a[i][k],r[j][k])
                    m=complexSum(temp,m)
                ans[i][j]=m
    return ans

def conjugadoVector(a):
    ans=[0*len(a) for n in range(len(a))]
    for i in range(len(a)):
        
        ans[i] = complexConj(a[i])
    return ans 

def multiVectores(a,b):
    ans = (0,0) 
    for i in range(len(a)):
        ans = complexSum(ans,complexProduct(a[i],b[i]))
    return ans
    
def innerProduct(a,b):
    v1 = conjugadoVector(a)
    return multiVectores(v1,b)

def normaVector(a):
    norma = innerProduct(a,a)
    return math.sqrt(norma[0])

def distanciaVectores(a,b):
    resta = restaVectores(a,b)
    return normaVector(resta)
def esUnitaria(a):
    adjunta = dagaMatriz(a)
    ans = matrixProduct(a,adjunta)
    for i in range(len(a)):
        for j in range(len(a[0])):
            num = ans[i][j]
            if(i==j and (num[0]!=1 or num[1]!=0)):
                return False
            elif(i!=j and (num[0]!=0 or num[1]!=0)):
                 return False
    return True
def esHermitiana(a):
    adjunta = dagaMatriz(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]!=adjunta[i][j]):
                return False
    return True
def productoTensorVectores(a,b):
    ans = []
    for i in range(len(a)):
        for j in range(len(b)):
            ans.append(complexProduct(a[i],b[j]))
    return ans 
def accionmatrizvector(matrix, vector):

    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [[0, 0] for x in range(row)]

        for i in range(row):
            for j in range(col):
                multi = complexProduct(matrix[i][j], vector[j])
                answ[i] = complexSum(answ[i], multi)

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def accionvectormatrizboolean( matrix, vector ):
    row, col  = len( matrix ), len( matrix [ 0 ] )
    length = len( vector )

    if  ( col == length ):
        answ = [ False for c in range( row  ) ]

        for i in range( row ):
            And = True
            
            for j in range( col ):
                And = matrix[ i ][ j ] and vector[ j ]  
                answ [ i ] = answ[ i ] or And
            
        return answ 
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
def identityMatrix( matrix ):
    row,  column  = len( matrix ) , len( matrix[ 0 ] )
    
    matrix=[[[] for i in range( column )] for j in range( row )]
    
    for i in range( row ):
        for j in range(  column ):
            if i==j:
                matrix[ i ][ j ] =  [ 1,0]
            else:
                matrix[ i ][ j ] =  [ 0,0 ]
    return matrix