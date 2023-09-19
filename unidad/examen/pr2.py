while True:
    n1 = input("Ingrese n1: ")
    n2 = input("ingrese n2: ")
    if n1.isdigit() and n2.isdigit():
        n_1 = int(n1)
        n_2 = int(n2)
        if n_1 > 99 and n_2 >99:
            break
        else:
            print("ingrese un numero entero positivo")
    else:
        print("ingrese un numero valido entero")

f_1= n1[::-1]
f_2=n2[::-1]
f1= 0
f2=0
lista1 = []
lista2 = []
for i in n1:
    lista1.append(i)
for i in n2:
    lista2.append(i)
lista1.reverse()
lista2.reverse()
num1= ""
num2 = ""
for x in lista1:
    num1= num1 + x
for x in lista2:
    num2 = num2 + x
num1 = int(num1)
num2 = int(num2)
if num1 > num2:
    print(num1)
else:
    print(num2)
