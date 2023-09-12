diccionarioEpico = {}
Palabra= str(input("Ingrese las palabras: "))
PalabraEpica = Palabra.split()
for x in PalabraEpica:
    if diccionarioEpico.get(x) == None:
        diccionarioEpico[x] = 1
    else:
        diccionarioEpico[x] = diccionarioEpico[x] + 1
print(diccionarioEpico)