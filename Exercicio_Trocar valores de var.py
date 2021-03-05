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

print ('Antes da troca o VA era {} e o vB era {}'.format(vA,vB))
vC = vA # A gente guarda o valor de vA para não se perder
vA = vB # Coloca o valor de vB no vA
vB = vC # Pega o valor que era do vA de dentro do vC
print ('Depois da troca o VA sera {} e o vB sera {}'.format(vA,vB))

########################ou##########################################
va = float(input('digite vA: '))
vb = float(input('digite vB: '))
va , vb = vb , va
print('va era {} e vb era {} agora va é {} e vb é {}' .format(vb,va,va,vb))
