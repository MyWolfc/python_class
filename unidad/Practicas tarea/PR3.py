NombreEpico = str(input("Ingrese su nombre: "))
print(NombreEpico)
ListaEpica = list(NombreEpico)

for x in range(0,len(ListaEpica)):
    if (x%2) == 0:
        ListaEpica[x] = ListaEpica[x].lower()
    else:
        ListaEpica[x] = ListaEpica[x].upper()
cadena = ""
for l in reversed(ListaEpica):
    cadena = cadena + " " +l
print(cadena)
