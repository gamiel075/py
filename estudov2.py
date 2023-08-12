

valor_total= float(input('digite o valor da compra'))
cupon_desconto = input('qual a letra do cupom')



if(cupon_desconto == 'a' or 'A'):
    valo_final = valor_total - 100


else:
    valo_final = valor_total  


if(cupon_desconto == 'b' or 'B'):
    valo_final = valor_total - 200


else:
    valo_final = valor_total  


if(cupon_desconto == 'c' or 'C'):
    valo_final = valor_total - 300


else:
    valo_final = valor_total  








print ('o valor final é de {} ' .format(valo_final))
