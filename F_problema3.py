print("Adunarea a doua fractii:")
a,b=int(input('prima fractie: ')),int(input("supra "))
c,d=int(input('a doua fractie: ')),int(input("supra "))
def adunare(x,y,z,w):
    s=((x*w)+(z*y))/(y*w)
    return (s)
print(a,'/',b,'+',c,'/',d,'=',adunare(a,b,c,d))

print("inmultirea a doua fractii:")
a,b=int(input('prima fractie: ')),int(input("supra "))
c,d=int(input('a doua fractie: ')),int(input("supra "))
def inmultire(x,y,z,w):
    m=(x*z)/(y*w)
    return (m)
print(a,'/',b,'*',c,'/',d,'=',inmultire(a,b,c,d))    
