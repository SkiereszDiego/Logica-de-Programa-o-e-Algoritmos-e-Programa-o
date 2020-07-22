'''
2.	Escreva um algoritmo que leia dois números que deverão ser colocados,
    respectivamente nas variáveis vA e vB.  O algoritmo deve, então, trocar os
    valores de vA por vB e vice-versa. 
    Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da 
    troca e após a troca.
'''

vA = int(input("digite um numero:"))
vB = int(input("digite outro numero:"))
vC = 0

print ("Antes da troca o","vA era ",vA,"e o vB era ", vB)

vC = vA # A gente guarda o valor de vA para não se perder
vA = vB # Coloca o valor de vB no vA
vB = vC # Pega o valor que era do vA de dentro do vC


print ("Depois da troca o","vA fica ",vA,"e o vB sera ", vB)