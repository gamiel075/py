''''soma = 0
pergunta = 1

while (pergunta <= 5):
    x = float(input('digite a renda da {}loja'.format(pergunta)))
    soma = soma + x
    pergunta = pergunta + 1


despesa = float(input('digite suas despesas'))
lucro = soma - despesa
print('seu lucro final é de %.2f ' %(lucro))'''


''' =1
x = int(input('Digite o valor inicial'))
while (x <= 100):
    if(x % 2 ==0):
        print(x)
    x = x + 1 '''

'''soma = 0
cont = 1

while (cont <= 5):
    x = float(input('digite o valor do lucro da  {} loja'.format(cont)))
    soma =  soma + x
    cont = cont + 1
lucro = soma
print('seu lucro  final é de %.2f ' %(lucro))'''


'''x = float(input('digite o valor incial'))


while(x <245):
    
    x = x + 1
    print(x)'''

soma = 0
cont = 1

while (cont <= 3):
    x = float(input('digite {} o valor'.format(cont)))
    soma = soma + x
    cont = cont + 1 



if(soma <50):
        print('este é um numero pequeno')
        print(soma)

elif(soma > 50 and soma < 100):
        print('este é um numero médio')
        print(soma)

elif(soma > 100 or soma <= 150):
        print('este é um  numero grande')
        print(soma)

elif(soma > 150 and soma <200):
        print('este é um numero muito grande')
        print(soma)



