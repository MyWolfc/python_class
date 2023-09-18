import csv
from operator import itemgetter
def OrdenarNom(rarete):
    diccionario_ordenado = sorted(rarete, key=itemgetter("Nombre"))
    nombre_archivo ="OrdenadoNombre.csv"

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        campos = ["Numero de control","Nombre","Calificacion"]
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        escritor_csv.writeheader()
        # Escribir los datos en el archivo
        for fila in diccionario_ordenado:
            escritor_csv.writerow(fila)
        return diccionario_ordenado

    return diccionario_ordenado


def OrdenarCalif(rarete):
    diccionario_ordenado = sorted(diccionario, key=lambda x: x["Calificacion"])
    nombre_archivo ="OrdenadoCalif.csv"

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        campos = ["Numero de control","Nombre","Calificacion"]
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        escritor_csv.writeheader()
        # Escribir los datos en el archivo
        for fila in diccionario_ordenado:
            escritor_csv.writerow(fila)
        return diccionario_ordenado

def OrdenarNum(rarete):
    diccionario_ordenado = sorted(rarete, key=itemgetter("Numero de control"))
    nombre_archivo ="OrdenadoNum.csv"

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        campos = ["Numero de control","Nombre","Calificacion"]
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        escritor_csv.writeheader()
        # Escribir los datos en el archivo
        for fila in diccionario_ordenado:
            escritor_csv.writerow(fila)
        return diccionario_ordenado

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
    


