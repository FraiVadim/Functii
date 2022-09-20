x=int(input("Dati numar intreg "))
y=int(input("Dati numar intreg "))

def cmmdc(n,m):
    while(n != m):
        if(n > m):
            n=n-m
        else:
            m=m-n
    return m

def cmmmc(n,m):
    r=(n*m)/cmmdc(x,y)
    return int(r)

def cinci_multipli(n,m):
    multipli=[]
    for i in range(1,6):
        multipli.append(cmmmc(x,y)*i)
    return multipli

print(cinci_multipli(x,y))