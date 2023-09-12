def Reglas(matrizepica):
    matrizEspejo = []
    for f in matrizepica:
        nuevafila = []
        for f1 in f:
            if f1 == 0:
                nuevafila.append(0)
            elif (f1%3)== 0 and f1%5 == 0:
                nuevafila.append(4)
            elif f1%3 == 0:
                nuevafila.append(2)
            elif f1%5 == 0:
                nuevafila.append(3)
            else:
                nuevafila.append(0)
            pass
        matrizEspejo.append(nuevafila)
    return matrizEspejo
matriz = []
for x in range(0,5):
    fila = []
    for y in range(0,4):
        numero = int(input(f"Agregar numero en {x} {y}: "))
        fila.append(numero)
    matriz.append(fila)
print(matriz)
print(Reglas(matriz))