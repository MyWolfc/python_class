
n = int(input("Ingrese la minima "))
segmentos = 0
segmentos2 = 0
for x in range(0,n):
    print(n,pow(2,x))
    if  pow(2,x)> n:
        segmentos = pow(2,x)
        segmentos2 = pow(2,x)
        break

#print(segmentos)

bandera = True
res = 0
axu = 0
while bandera:
    #print(segmentos)
    segmentos = int(segmentos/2)
    axu= axu+1
    print(f"res: {res} segmentos: {segmentos} axu: {axu}")
    if res+segmentos < n:
        #axu=axu+1
        res+=segmentos
        print(f"res: {res} segmentos: {segmentos} axu: {axu}")
    if res+segmentos > n:
        print("se pasa")
        aux = res+int(segmentos/2)
        print(f"res: {res} segmentos: {segmentos} axu: {axu}")
        if aux == n:
            axu=axu+1
            res +=int(segmentos/2)
            print(f"res: {res} segmentos: {segmentos} axu: {axu}")
            break
    elif res == n:
        break
    if segmentos ==1:
        bandera = False


print(segmentos2,axu)