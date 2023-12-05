#FUNÇÃOCOMINDICADORES


def a ():
    somax2=0
    for x in range(1,11):
        somax1 = float(input('digite o  numero de vendas fo vendedor {}'.format(x)))
        somax2+= somax1
    print(somax2)
    return somax2

def b (somax2):
    conta = somax2 - 100000
    print(conta)
    return conta

def c (somax2):
    mediaxpessoa = somax2 / 10
    print(mediaxpessoa)
    
def d (conta):

    if(conta > 100000):
        print('saldo positivo')

    if(conta < 100000):
        print('saldo negativo')




resultado_a = a()
resultado_b = b(resultado_a)
c(resultado_a)
d(resultado_b)
