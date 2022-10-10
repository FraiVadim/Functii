from random import randint
n=int(input('dati numarul de generari: '))
lista=[]
suma=0
for i in range(n):
    a=randint(1,100)
    print(a)
    lista.append(a)
    suma=suma+a
print('Suma fara elementul maxim:',suma-max(lista))