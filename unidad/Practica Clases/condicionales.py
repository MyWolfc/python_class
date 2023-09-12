PizzaDe = int(input("\n/////////////////////\nSelecione el tipo de pizza: \n1.-Vegetariana\n2.-No vegetariana "))
if PizzaDe == 1:
    
    IngredienteEpico = int(input("\n---------------------\nSelecione el ingrediente: \n1.-Pimiento\n2.-Tofu "))
    IngredienteEpico = "Pimiento" if IngredienteEpico == 1 else "Tofu"
    ListaEpica = ["Pizza vegetariana",IngredienteEpico,"Tomate","Mozarrella"]
    print(ListaEpica)

elif PizzaDe == 2:
    IngredienteEpico = int(input("\n---------------------\nSelecione el ingrediente: \n1.-Peperoni\n2.-Salami \n3.Carne "))
    if IngredienteEpico == 1:
        ListaEpica = ["Pizza vegetariana","Peperoni","Tomate","Mozarrella"]
        print(ListaEpica)
    elif IngredienteEpico == 2:
        ListaEpica = ["Pizza vegetariana","Salami","Tomate","Mozarrella"]
        print(ListaEpica)
    else:
        ListaEpica = ["Pizza vegetariana","Carne","Tomate","Mozarrella"]
        print(ListaEpica)
else:
    print("selecione una opcion valida")
