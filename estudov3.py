


#avaliação



idade_candidato = int(input('digite sua idade'))
cidade_candidato = input('digite sua cidade')
nome_candidato = input('digite seu nome')
sobrenome_candidato = input('digite seu sobrenome')
formação_candidato = input('digite sua formação')
nota_exame1 = float(input('digite sua nota'))
nota_avaliacao = int(input('digite a nota da avaliacao pessoal'))
nota_final = nota_avaliacao + nota_exame1 / 2

if (idade_candidato > 20):
    print('sua idade se encontra aprovada')
else:
    print('desculpe mas voce nao tem idade suficiete')


if(cidade_candidato == 'franco da rocha' or 'francisco morato' or 'caieiras'):
    print('sua cidade é proxima do local da vaga')

else:
    print('desculpe mas vc nao mora perto de nossa empresa')

if(nota_final >= 6):
    print ('vc foi aprovado em nossos testes')


else:
     print('desculpe mas vc não foi aprovado')



print('ola {} seja bem vindo'. format(nome_candidato + '  ' + sobrenome_candidato))
print('entraremos em contato para mais informações')







