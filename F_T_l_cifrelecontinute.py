x=int(input("Dati numar intreg "))
y=int(input("Dati numar intreg "))

def cifr_comune(n,m):   
    m=(set(str((n)))).intersection(set(str(m)))
    return print('cifre comune sunt:',m)

print(cifr_comune(x,y))