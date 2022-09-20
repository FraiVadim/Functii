a=int(input("Dati numar intreg: "))
b=int(input("Dati numar intreg: "))
def cmmdc(n,m):
    while(n != m):
        if(n > m):
            n=n-m
        else:
            m=m-n
    return m

print(cmmdc(a,b))