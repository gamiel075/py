

#maior programa, imitação do wms

Lucro_mensal = float(input('digite a renda bruta da loja'))
Despesas = float(input('digite aqui o valor conrespondente ás suas despesas mensais'))
Lucro_final = Lucro_mensal - Despesas
 
Aviso = ' neste mês a sua loja lucrou %.2f' %(Lucro_final)
print(Aviso)

Estoque = float(input('digite aqui o valor total para reposição'))
Lucro2 = Lucro_final - Estoque

Folha = float(input('digite aqui a sua folha de pagamento'))
Lucro3 = Lucro2 - Folha

if(Lucro_final < 300000 ):
    print('atenção as vendas estão em queda')

else:
    print('as vendas estão ótimas')

conta = Despesas - Estoque - Folha

if(conta <= 160000 ):
   print('as despesa estão controláveis ')
   print('a sua renda final é de %.2f'%(Lucro3))

elif(conta >= Lucro3 ):
    print('a  operação esta negativa')
    print('a sua renda final é de %.2f'%(Lucro3))

















