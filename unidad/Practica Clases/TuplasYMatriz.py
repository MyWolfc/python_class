a = [[1,2,3],[4,5,6]] 
b = [[-1,0],[0,1],[1,1]]
def productoEpico(m1,m2):
    suma1,sumaaux2,suma3,sumaaux4 = 0,0,0,0
    for x in range(0,len(m1)):
        for y in range(0,len(m1[x])):
            if x == 0:
                multi = m1[x][y] * m2[y][x]
                suma1 = multi + suma1
                multi2 = m1[x+1][y] * m2[y][x]
                suma3 = suma3 + multi2
            else:
                multi = m1[x-1][y] * m2[y][x]
                sumaaux2 = multi + sumaaux2
                multi2 = m1[x][y] * m2[y][x]
                sumaaux4 = sumaaux4 + multi2
    tuplafinal = (suma1,sumaaux2),(suma3,sumaaux4)
    return tuplafinal
tupla1 = productoEpico(a,b)
print(tupla1)