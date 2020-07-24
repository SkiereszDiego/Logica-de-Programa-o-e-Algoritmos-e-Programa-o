'''7.	Ler 3 números e imprimi-los em ordem crescente.'''

a = float(input("digite um numero:"))
b = float(input("digite outro numero:"))
c = float(input("digite outro numero:"))

'''
Pensar em todas possibilidades primeiro
'''

if (a>b and b>c and a>c):
    print(a,b,c)
elif (a>b and b<c and a>c):
    print(a,c,b)
elif ():
    print(b,a,c)
elif ():
    print(b,c,a)
elif ():
    print(c,b,a)
else:
    print(c,a,b)