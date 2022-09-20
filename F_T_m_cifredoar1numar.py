x=int(input("Dati numar intreg "))
y=int(input("Dati numar intreg "))

def cifr_primul_da_doi_nu(n,m):   
    m=(set(str((n)))).difference(set(str(m)))
    return print('cifre ce sunt in primul ,dar in al doilea nu sunt:',m)

print(cifr_primul_da_doi_nu(x,y))