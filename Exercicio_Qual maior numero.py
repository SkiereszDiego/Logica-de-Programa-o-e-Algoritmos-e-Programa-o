'''6.	Fazer um algoritmo para ler dois números e mostrar o maior deles.'''

a = float(input("digite um numero:"))
b = float(input("digite outro numero:"))

if ( a > b):
    print ( "O maior numero é o ", a)

elif ( a == b):
    print ('Os numeros são iguais!')

else:
    print ('O maior numero é o ', b)
