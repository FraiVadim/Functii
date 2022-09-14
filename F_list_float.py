def creare_lista():
    n=int(input("Nr. de elemente de tip float=?"))
    lista_locala=[]
    for i in range (n):
        elem=input('elementul '+str(i)+' este:')
        if type(elem)==float:
            lista_locala.append(elem)
        else:
            print("eroare")
    return lista_locala    
lista1=creare_lista()
print(lista1)