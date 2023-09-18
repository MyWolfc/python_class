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
