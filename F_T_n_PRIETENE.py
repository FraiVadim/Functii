x=int(input("Dati numar intreg "))
y=int(input("Dati numar intreg "))

def PRIETENE(n,m):
    d=1
    listn=[]
    while d<=n:
        if n%d==0:
            listn.append(d)
            d=d+1
        else:
            d=d+1
    d=1
    listm=[]
    while d<=m:
        if m%d==0:
            listm.append(d)
            d=d+1
        else:
            d=d+1
    if len(listn)==len(listm):
        return('PRIETENE')
    else:
        return('NU SUNT PRIETENE')

print(PRIETENE(x,y))