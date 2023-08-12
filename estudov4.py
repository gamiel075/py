# calculo de inflação


ano_atual = int(input('digite o ano atual'))
ano_compra = int(input('digite o ano de compra'))
valor_produto = float(input('digite o valor'))

anos =  ano_compra - ano_atual
taxa_inflacionaria = valor_produto * 0.2
ano_taxa = anos * taxa_inflacionaria 
valor_final =  valor_produto + ano_taxa


valor= 'o produto custará %.2f' %(valor_final)

print('dentro de {} anos o valor do produto sofrerá uma alteração '.format(anos))
print(valor)


