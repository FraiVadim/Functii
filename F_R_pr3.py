from random import randint
k=[]
a=randint(0,999999999)
print(a)
while a>0:
    r=a%10
    a//=10
    k.append(r)
print('0 a aparut de',k.count(0),'ori')
print('1 a aparut de',k.count(1),'ori')
print('2 a aparut de',k.count(2),'ori')
print('3 a aparut de',k.count(3),'ori')
print('4 a aparut de',k.count(4),'ori')
print('5 a aparut de',k.count(5),'ori')
print('6 a aparut de',k.count(6),'ori')
print('7 a aparut de',k.count(7),'ori')
print('8 a aparut de',k.count(8),'ori')
print('9 a aparut de',k.count(9),'ori')
