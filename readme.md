primeiro = 10 
segundo = 45


print( 'primeiro' + 'segundo')

saída = primeirosegundo


\* o codigo acima é uma variação do comando 'print' onde as palavras estão sendo juntadas em uma \*

primeiro = 10 
segundo = 45



print( primeiro + segundo)

saída = 55

\* verdadeiro ou falso \*

verdade = 2 < 5
print(verdade)

saída = true

\* operadores \*


a = 10
b = 20

resposta = a == b
print(resposta)
saída = false


o sinal de '=' diz respeito á atribuir um valor á um dado e\ou váriavel, já o '==' diz 
respeito a comparação de igualdade

Em Python, números inteiros são da classe int e números reais são da classe float (pois a representação de números reais é realizada em notação com ponto ...

\* varíaveis strig \*

resultado = 'hello word'



print(resultado [2])

saida = l

\* concatenação de strigs \*

n1 =  'GABRIEL'
n1 = n1 + ' ferreira'

print(n1)

saida = GABRIEL ferreira

\* multiplicação de caracteres \*

gabriel = 'ferreira'
bezerra = gabriel + ' ' + '&' * 6  + ' bezerra'

print(bezerra)
saída = ferreira &&&&&& bezerra

\* composição ou substituir na string \*



nota = 7.6

s1 = 'voce tirou nota %.2f na nota de biologia' % nota

print(s1)


saida: voce tirou nota 7.60 na nota de biologia

atraves do comando %f conseguimos substituir uma variavel , e se colocamos %.2f, não ira aparecer muitos numeros depois da virgula como '7.60000000' , porque assim serão dois numeros depois da virgula


nota = 7.6
nota2 = 7.8
s1 = 'voce tirou nota %.2f na nota de biologia e %.1f em artes' %( nota , nota2)

print(s1)


saida: voce tirou nota 7.60 na nota de biologia e 7.8 em artes


\* composição moderna \*

Uma maneira mais simples de fazer a composição acima



nota = 7.6
nota2 = 7.8

s1 = 'voce tirou  {} em biologia e {} em artes' .format(nota,nota2)

print(s1)

saída = voce tirou  7.6 em biologia e 7.8 em artes

\* fatiamento \*

recorte e impressão de caracteres

s1 = 'gabriel ferreira bezerra'
print (s1 [0:5])

saida = gabri

\* numero de caracteres \*

gabriel = 'bezerra'
tamanho = len(gabriel)

print(tamanho)

saida = 7

este comando serve para identificar o numero de caracteres em uma strig





