def Total(*Productos):
    sumaTotal =0
    ProductosTotal = len(Productos)
    for l in Productos:
        sumaTotal+= l
    return sumaTotal,ProductosTotal

print(Total(2,3,4,5,6,7,8,9,10))

que = 4%2
print(que)
