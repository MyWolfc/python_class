
import csv
import random


def split(Lineinput,Lineoutput,Linea):
    with open(file='c') as file:
        nombre = file.readline().strip();
        outputFile = None
        lineacount = 0
        for linea in file:
            if Lineinput % Linea:
                if Lineoutput is not None:
                    outputFile.close()


if __name__ is "__main__":
    split()

numerorandom = random.randint(1,10)
print(numerorandom)
while True:
    numero = int(input("inserte un numero"))
    if numero == numerorandom:
        break;
    if numero > numerorandom:
        print("te pasaste")
    else:
        print("numero es menor")

print("numero correcto")