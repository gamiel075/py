'''x = 1
x += 10
print (x)'


SAIDA  11
'''

'''x = 20

x /= 10

print(x)

SAIDA= 2.0

'''

'''soma = 0 
cont = 1

while (cont <= 4 ):
    x= float(input('digite o valor da {} nota'. format(cont) ))

    soma += x
    cont += 1

soma /= 4
print(soma)'''




#validador

'''x = int(input('digite um valor impar'))
while(x % 2 == 0):
    x = int(input('digite um valor impar'))
print('vc acertou, encerrando programa.....')'''


#interronpendo programa com break


'''print('Digite um texto para aparecer na tela,para sair digite SAIR')

while True:
    texto = input('')
    print(texto)
   
    if texto == 'sair':
        print('encerrando programa')
        break'''



#login com senha

'''while True:

    nome = input('digite seu nome')
    if(nome != 'gabriel'):
        continue
    senha = input('digite sua senha')
    if(senha == 'ferreira'):
        print('bem vindo')
        break'''

 #truty e falsey

nome = ''
while not nome:
    nome = input('digite o seu nome')

valor = int(input('digite o valor'))
if valor:
    print('vc digitou um valor diferente de zero')

else: 
    print('voce digitou zero')



 






