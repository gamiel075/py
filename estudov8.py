#estrutura de repetição#

"""x = 10
while(x <= 100):
    print(x)
    x =  x + 10 """

"""x = 2
while(x <= 20):
    print(x)
    x = x + 2"""


#contadores

'''inicial = int(input('digite o numero inicial'))
final = int(input('digite o numero final'))

x = inicial  
while (x <= final):
    if(x % 2 == 0):
        print(x)
    x = x + 1 '''

soma = 0
cont = 1

while (cont <= 5):
    x = float(input('digite sua {}nota'.format(cont)))
    soma = soma + x
    cont = cont + 1

media = soma/5
print('sua nota final é de %.2f ' %(media))



