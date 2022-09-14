n=int(input("Introdu n: "))
m=int(input("Introdu m: "))
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return int(fact)
if (n>m):
    print("C=",factorial(n)/(factorial(m)*factorial(n-m)))