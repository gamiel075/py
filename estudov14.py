#tabuada em for

'''x = tabuada'''

'''for tabuada in range (1,11,1):
    print('tabuada do {}'.format(tabuada))

    for x in range (1,11,1):
        print(' {} * {} =  {}'.format(tabuada,x, tabuada * x))'''




#analíse a estrutura acima e faça um reformulaçao para uma nova resolução para um novo problema

'''for i in range(1, 6):
    distancia_metros = float(input('Digite a distância percorrida em metros no carro {}: '.format(i)))
    distancia_km = distancia_metros / 1000
    print('A distância em km é: {:.2f} km'.format(distancia_km))'''

soma_km = 0  # Inicialize a variável para a soma

for i in range(1, 6):
    distancia_em_metros = float(input('Digite a distância percorrida em metros no carro {}: '.format(i)))
    distancia_em_km = distancia_em_metros / 1000
    soma_km += distancia_em_km  # Adicione a distância em quilômetros à soma
    print('A distância em km é: {:.2f} km'.format(distancia_em_km))

media_km = soma_km / 5  # Calcule a média

print('A soma de todas as distâncias em km é: {:.2f} km'.format(soma_km))
print('A média das distâncias em km é: {:.2f} km'.format(media_km))

