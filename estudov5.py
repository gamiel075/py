



#lucratividade x produtividade
# a seguir voce vera uma analise de lucro x produtividade#


lucro_primeira = float(input('digite seu lucro na primeira loja'))
lucro_segunda = float(input('digite seu lucro na segunda loja'))
lucro_terceira = float(input('digite seu lucro na terceira loja'))
lucro_quarta = float(input('digite seu lucro na quarta loja'))

lucro = lucro_primeira + lucro_segunda + lucro_terceira + lucro_quarta

produçao_primeira = float(input('digite sua produçao na primeira loja'))
produçao_segunda = float(input('digite sua produçao na segunda loja'))
produçao_terceira = float(input('digite sua produçao na terceira loja'))
produçao_quarta = float(input('digite sua produçao na quarta loja'))



produçao = produçao_primeira + produçao_segunda + produçao_terceira + produçao_quarta

#há sempre uma diferença entre renda líquida e renda bruta,á diferença se dá pela existencia de despesas

variança = produçao - lucro 
renda_líquida = produçao - variança



lucro_estimado1 = 1000000
#este valor é uma estimativa de um aumento da produção e\ou numero de vendas baseado no controle de estoque

lucro_estimado2 = 750000
#o valor deste é o valor médio calculado á partir do ultimos 4 meses do ano da loja

if(renda_líquida > lucro_estimado1):
    print('sua renda esta sendo positiva tendo margem de crescimento')

elif (renda_líquida >= lucro_estimado2):
    print('sua renda sem encontra em uma moderada margem de crescimento')

elif (renda_líquida < lucro_estimado2 ):
    print('suas vendas e sua produtividade estão em massiva queda')



renda = 'a sua renda líquida final é de  %.2f ' % (renda_líquida)
print(renda)
despesas = 'vc  gastou %.2f em despesas'% (variança)
print(despesas)


Bruta = 'sua Renda bruta é de %.2f ' % ( produçao)
print(Bruta)

dispesa_extra = float(input('digite o valor das despesas  extras  cujo débito foi incluido mas não catalogado'))


RendaXdespesa = variança - dispesa_extra
Rendaxdespesa1 = 'Suas despesas casuais  menos sua despesas extras deste mês é de %.2f ' % ( RendaXdespesa)
print(Rendaxdespesa1)



pergunta1 = input(('o Resultado foi satisfátorio'))

if(pergunta1 == 'nao' and 'NAO'):
    print('elabore novos métodos, estratégias de para a operação')

else:
    print('sua loja esta em constante crescimento parabéns')



