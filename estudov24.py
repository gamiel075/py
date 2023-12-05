
def autenticador():
    while True:
        nome = input('digite seu nome')
        if (nome != 'gabriel'):
            continue

        senha = 'bezerra'
        senha2 = input('digite a senha')
        if(senha2 == senha):
            break


listadecompra = []
for i in range(4):
    nome = input('digiye o nome')
    qtd = int(input('digite a quantidade'))
    valor = float(input('digite o valor'))
    total = valor * qtd
    listadecompra.append([nome,qtd,total])

print(listadecompra)
