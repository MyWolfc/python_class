print("Hola mundo")
print("AYUDA NO SE AL PYTHON")
#Numero Entero
x = 1
#Numero Flotante
y = 2.2
#Numero Complejo
z = 2j

VARIABLE = "cadena"
#con Type podemos ver que tipo de dato es
print(type(z))
#con esto podemos saber como parsear el dato
y = float(x)

#Investiga como hacer diccionario
print(x)
print(y)
print(z)
#Boleanos
V =1
F = 0
#condicion IF
if V:
    print("Verdadero")
else:
    print("Falso")

#Cadenas son inmutables
Cadenas = "Hola Mundo"
Cadena_epica = f"Hola mundo{y}"
print(Cadena_epica);
#cadena multilinea**


Cadena= "Hola mundo \nAdios"
#print tenemos dos funcione end y sep
print(Cadena)
print(Cadena)



#funciones
nombre = "Eduardo Leyva"
nombre:-1
print(nombre)
print(nombre[-1])
#Tupla son ordenadas e inmutable y permite datos duplicados
tupla =(1,2,3)
print(type(tupla))
print(tupla)
tuplas = 1,2,('a','b'),3
print(tuplas)
print(tuplas[3])
#una manera de agregar datos a una tupla es convertiendolo en una lista
lista = list(tupla)
lista.append(4)
print(lista)
for i in tupla:
    print(i)

#r,s,t,a = tupla
#print(r,s,t,a)
#si una tupla solo tiene un elemento lo tomara como una variable de tipo de dato 
#si queremos hacer duplas con un solo elemento debemos poner una coma al final
tupla = (2,)
print(tupla)
print(type(tupla))

#contar tuplas
tupla = (2,6,5,9,6,3)
print(tupla.count(2))

#LISTAS

Listas = [1,2,3,4]
print(Listas)
Listas2 = list('4567')
print(Listas2)

Lista3= [1,2,4,[10,11,12],5]
print(Lista3 [2])


Lista4 = [1,2,3,4,5,6,7,8,9]
print(Lista4[0:2])
print(Lista4[2:0])

Lista4[0:3] = [0,0,0]
ListasAux = Listas

for i in Listas:
    print(i)

for index,l in enumerate(ListasAux):
    print(index,l)

#for i in range(0,len.Lista3):
#    print(Lista3[l])

Lista3.append(3)
Lista3.extend([2,1])
Lista3.insert(1,4)
Lista3.pop(1)


#SET
#son mutables e imnutables a la vez
#puedo agregar nuevos datos pero no puedo modificar los elementos del set
set1 ={1,3,4,2}
print(set1)
#no deja cambior sus elementos
#set[0] = 2

#pero si deja agregar elementos y eliminar
set1.add(5)
print(set1)
set2 = set([1,2,3,4,5,6,7])
print(set2)

for l in set1:
    print(l)

s1 = {1,2,3}
s2 = {3,4,5}

print(s1|s2)

print(s1^s2)

s1.add(4)
#elimina pero se rompe si no existe
s1.remove(1)
#verifica que existe y lo elimina
s1.discard(5)
s1.pop()
s1.clear()
s1.union()
s1.intersection()

#diccionarios son estructuras no ordenadas son indexaddas
dicc = {'nombre':'juan','Edad':'22'}


print(dicc["nombre"])
print(type(dicc))

print(dicc)

print(type(dicc))

for l in dicc:
    print(dicc[l])

#.aeris
print(dicc.get('nacionalidad'))
dicc.popitem()

for l in dicc:
    print(dicc[l])

#if

X = 18
if(X >= 18):
    print("tiene mas 18")
elif(X <= 10):
    print("tiene entre 18 y 30 años")
else:
    print("xd")

if(X >= 18): print(X); print(y)
#carnario
#if(X >= 18) else  print(X)

#for
caddna=  "hola mundo"
for l in caddna:
    print(l)

for X in range(0,100):
    #para reservar codigo
    pass
    if(X==50):
        print("llego al 50")
        #con continue llega al siguiente iteracion sin romper el ciclo
        continue
        #con break romper el ciclo directamente
        break
    print(X)

I = 0
while I < 6:
    print(I)
    I += 1
    if(I == 2):
        print("llego a 2")
        break
else:#este el solo se complira si se cumplio el ciclo while si se rompe antes no se ejecuta
    print("Termino")

try:
    xd = 0
    xd/0
    print(xd)
except Exception:
    print(Exception);


def metodoEpico():
    Lepica= 0
    for a in  range(0,10):
        Lepica = a
    return(Lepica)

print(metodoEpico())
 
D = 10
F = 20

#podemos asignar el valor de un parametro estatico y se queda como posicion se puede ejecutar
def Multiplicar(x,y,c=1):
    return(x*y*c)

print(Multiplicar(D,F))

listaepica2 = [2,3,4,5]
print(type(listaepica2))

def ImprimirLista(x):
    for l in x:
        print(l)
    return

#cuando tratemos de mandar un objeto con un *
ImprimirLista(listaepica2)

def suma(*numerossum):
    print(type(numerossum))
    sumas = 0
    for l in numerossum:
        sumas=+l
    return sumas

print(suma(1,2,3,4,5,6))
##cuando se coloca con doble * significa que seran con llaves se convierte en diccionario

def suma2(**num):
    print(type(num))
    
    return 0

#print(suma2({1,2,3,4,5,6}))
di = { 'a' : 10, 'b' : 12,'c': 13}

numerose = list(range(1,101,))
print(type(numerose))
#x = lambda

def multiplicacion(n):
    return lambda a:print(n*a)

multiplicador = multiplicacion(2)
triplicador = multiplicacion(3)
print(multiplicador(2))
print(triplicador(2))

try:
    uma = 1/0
except Exception as e:
    print(e)
else:
    print("jalo")
finally:
    print("Como quiera sigue el codigo")