var1=80
var2=180
def sumar(a,b):
    return a+b
resultado=sumar(var1,var2)
print(f'La suma de {var1} y {var2} es {resultado}.')

def restar(a,b=100):
    return a-b

print(restar(150,30))
print(restar(300))