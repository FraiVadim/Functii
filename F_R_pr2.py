from random import randint
n=int(input('dati numarul de aruncari:'))
sase=0
for i in range (n):
    a=randint(1,6)
    print(a)
    if a==6:
        sase+=1
print('Sase a aparut de',sase,'ori')
