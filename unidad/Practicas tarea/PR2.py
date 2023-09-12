#Primera solucion
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for x in range(0,len(abecedario)):
    if (x%2) !=0:
        abecedario[x] = " "
for x in abecedario:
    if x == " ":
        abecedario.remove(x)
print(abecedario)

#Segunda solucion
abecedarioEPICO = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ABorrar = set()
for l in range(len(abecedarioEPICO)):
    if (l+1)%2==0:
        ABorrar.add(l)
ABorrarEpico = list(ABorrar)
for x in reversed(ABorrarEpico):
    abecedarioEPICO.pop(x)

print(abecedarioEPICO)

# Crear una lista con el abecedario
Abecedario = list("abcdefghijklmnñopqrstuvwxyz")

# Eliminar letras en posiciones múltiplos de 2
indices_a_eliminar = [i for i in range(len(Abecedario)) if (i + 1) % 2 == 0]
for indice in reversed(indices_a_eliminar):
    Abecedario.pop(indice)

# Mostrar la lista resultante
print(Abecedario)

