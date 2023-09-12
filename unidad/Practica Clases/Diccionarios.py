diccionario = {"PLATANO":1.35,"MANZANA":0.80,"PERA":0.85,"NARANJA":0.7}

fruta = input("Ingrese la fruta: ")
fruta = fruta.upper()
kilos = int(input("Ingrese los kilos "))
if(diccionario.get(fruta) == None):
    print("Esa fruta no existe")
else:
    print(f"Fruta: {fruta} \n{diccionario[fruta]} X {kilos} = {diccionario[fruta] * kilos}" )
