diccionarioEpico = {}

while True:
    Asignatura = str(input("Ingrese la asignatura: "))
    Creditos = str(input("Ingrese los creditos: "))
    #print(f"la {Asignatura} tiene {Creditos} creditos")
    if Asignatura == ' ' or Creditos == ' ':
        break;
    else:
        diccionarioEpico[Asignatura] = Creditos;
ListaMaterias= [x for x in diccionarioEpico]
SumaTotal = 0
for x in diccionarioEpico:
    SumaTotal += int(diccionarioEpico[x])
    print(f"la asignatura {x} tiene {diccionarioEpico[x]} creditos")
print(f"-----------------------\nTotal de creditos: {SumaTotal} \n-----------------------\n{ListaMaterias}")