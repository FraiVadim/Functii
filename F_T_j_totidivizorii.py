x=int(input("Dati numar intreg "))
y=int(input("Dati numar intreg "))
def totidiv(n,m):
    while(n != m):
        if(n > m):
            n=n-m
        else:
            m=m-n
    d=1
    list=[]
    while d<=m:
        if m%d==0:
            list.append(d)
            d=d+1
        else:
            d=d+1

    return (list)
    

print('toti divizorii sunt:',(totidiv(x,y)))