x=int(input("Dati numar intreg: "))
y=int(input("Dati numar intreg: "))

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

print(cmmmc(x,y))