

salario = int(input('salario'))
ano_admissao = int(input('qual ano vc entrou nesta empresa'))
ano= int(input('em que ano estamos'))
tempo_serviço =  ano - ano_admissao

if ( tempo_serviço > 10 ):
    bonus = salario * 0.2

else:
    if (tempo_serviço > 5):
        bonus = salario * 0.2

    else:
        bonus = salario * 0.1  

print ('seu tempo nesta empresa é de {} anos ' .format(tempo_serviço))
print ('seu bonus é de {}'.format(bonus))
print('seu salário neste  mês será {}' .format(salario + bonus) )