# para x no intervalo de 6 vezes, ou seja imprimir o possível valor 6 vezes,vale
#resaltar que ele imprime sempre menos um o valor dos parenteses e ele sempre começa em 0.

'''for x in range (6): 
    print(x)'''

'''for x in range (10,100,10):
    print(x)'''

'''for x in range (100,0, - 10 ):'''
'''print(x)'''

'''soma = 0
cont = 0

for x  in range (1,101):
    if(x % 2 == 0):
        soma += x
        cont +=1
        
media = soma / cont
print(' a média dos numeros pares é {}'.format(media))'''

soma = 0
cont = 1


for x in range (1,6,1):

    x= float(input('digite o numero de gols do jogador {}'.format(cont)))
    soma += x
    cont +=  1

print('o saldo de gols de cada jogador é {}'.format(soma))

  
