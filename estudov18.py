#parametro são dados recebidos por uma função,e quando um dado é enviado chama-se passagem de parametro

'''s1 = '        gabriel'

def relatório(s1):
    print('|','__'*10 ,'|')
    print('|','__'*10 ,'|')
    print(s1)
    print('|','__'*10 ,'|')


relatório(s1)'''




'''def sub2(x,y):
    res = x - y
    print(res)

sub2(5,7)'''


'''def s2(x,y):
    conta = x - y
    return conta

x = float(input('digite o valor de x')) 
y = float(input('digite y'))

result = s2(x,y)
print(result)'''


#omissão de parametro

def soma(x=0,y=0,z=0,):
    res = x + y + z
    print(res)

soma(1,2)

