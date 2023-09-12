import datetime
datetimeOWO = datetime.datetime.now()
opcion = int(input("1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY\n"))
print(f"{datetimeOWO.year}/{datetimeOWO.month}/{datetimeOWO.day}") if opcion == 1 else print(f"{datetimeOWO.day}/{datetimeOWO.month}/{datetimeOWO.year}")