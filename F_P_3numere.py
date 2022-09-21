x=int(input("Dati numar intreg: "))
y=int(input("Dati numar intreg: "))
z=int(input("Dati numar intreg: "))
import math
def cmmdc(a,b,c):
    while(a != b):
        if(a > b):
            a=a-b
        else:
            b=b-a
    while(a != c):
        if(a > c):
            a=a-c
        else:
            c=c-a
    return c

def cmmmc(a,b,c):
    
    r=(a*b*c)/(cmmdc(x,y,z))
    return int(r)

def maximum(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c
        
def minimum(a,b,c):
    if a<b and a<c:
        return a
    if b<a and b<c:
        return b
    else:
        return c   

def totidiv(a,b,c):
    while(a != b):
        if(a > b):
            a=a-b
        else:
            b=b-a
    while(a != c):
        if(a > c):
            a=a-c
        else:
            c=c-a
    d=1
    list=[]
    while d<=a:
        if a%d==0:
            list.append(d)
            d=d+1
        else:
            d=d+1

    return (list)

def treicmmmc(a,b,c):
    
    r=(a*b*c)/(cmmdc(x,y,z))
    lista=[]
    lista.append(str(int(r)))
    lista.append(str(int(r*2)))
    lista.append(str(int(r*3)))
    return lista

def triunghi(a,b,c):

    if a+b>c and a+c>b and b+c>a:
        p=a+b+c
        sp=p/2
        aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        return('Aria:'+str(aria),'Perimetru:'+str(p)) 
    else:
        return('eroare')

def ecuatie(a,b,c):
    if (b**2)-(4*a*c)>=0:
        return ((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)),((-b-(math.sqrt((b**2)-(4*a*c))))/(2*a))
    else:
        return "eroare"

print(cmmdc(x,y,z))
print(cmmmc(x,y,z))
print(maximum(x,y,z))
print(minimum(x,y,z))
print(totidiv(x,y,z))
print(treicmmmc(x,y,z))
print(triunghi(x,y,z))
print(ecuatie(x,y,z))