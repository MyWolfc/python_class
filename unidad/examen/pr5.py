lista=[]
validar = True
x=1
cad2=""
palabras=""
while validar:
    cadena=input("ingrese la cadena: ")
    lista.append(cadena)
    cad2+=cadena+" "
    seguir = int(input("deseea seguir ingresando palabras\n1-.si \t 2-.no\n"))
    if seguir == 2:
        validar=False

for i in lista:
    print(i)
palabras=cad2.split()
ordenadas = sorted(palabras, key=lambda palabra: palabra)
cadFinal=""
numeros=""
for i in ordenadas:
    try:
        if int(i):
            numeros+=i+" "
    except ValueError:
        cadFinal+=i+" "
cadFinal=cadFinal+numeros
print(cadFinal)
