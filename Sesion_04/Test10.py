def multiplica(a,b,c=2):
    return a*b*c


print(multiplica(2,3,4))
print(multiplica(5,4))

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
num3=int(input("Ingrese un numero: "))
num4=int(input("Ingrese un numero: "))
l1=[]
def eval(a,b,c,d):
    l1.append(a)
    l1.append(b)
    l1.append(c)
    l1.append(d)
    l1.sort()
    return l1[-1]
def potencia(x):
    return pow(x,3)
res=eval(num1,num2,num3,num4)
print(potencia(res))
