import csv
from operator import itemgetter
def OrdenarNom(rarete):
    diccionario_ordenado = sorted(rarete, key=itemgetter("Nombre"))
    return diccionario_ordenado
    pass

def OrdenarCalif(rarete):
    diccionario_ordenado = sorted(diccionario, key=lambda x: x["Calificacion"])
    return diccionario_ordenado

    pass

def OrdenarNum(rarete):
    diccionario_ordenado = sorted(rarete, key=itemgetter("Numero de control"))
    return diccionario_ordenado
    pass



with open('C:\\Users\\Mein_\\Desktop\\CarpetaEpica\\Unidad\\Practica Clases\\Entrada.csv',newline='') as File:  
    reader = csv.reader(File)
    diccionario = []
    header = next(reader)
    for row in reader:
        fila ={
            "Numero de control": row[0],
            "Nombre":row[1],
            "Calificacion":int(row[2])
        }
        diccionario.append(fila)
        print(diccionario)
        diccionarioNom = OrdenarNom(diccionario)
        diccionarioCal = OrdenarCalif(diccionario)
        diccionarioNum = OrdenarNum(diccionario)
        print("-------------------------")
        for x in diccionarioNom:
            print(x)
        print("-------------------------")
        for x in diccionarioCal:
            print(x)
        print("-------------------------")
        for x in diccionarioNum:
            print(x)
    


