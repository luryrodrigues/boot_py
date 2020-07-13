#CÓDIGO 1
idade=int(input('Entre com a sua idade: '))
nova_idade=idade+1
print('No próximo ano você terá {} anos.'.format(nova_idade))

#CÓDIGO 2
lado_a=35
lado_b=14.33333
area_ret=(lado_a)*(lado_b)
print('O retângulo de lado A = %d e lado B = %.2f é %.3f '%(lado_a,lado_b,area_ret))

#CÓDIGO 3
lista_1=[1,2,'IGTI']
lista_2=[2,3,"Bootcamp"]
lista_3=lista_1+lista_2
print(lista_3)

#CÓDIGO 4
chute=int(input('Entre com um valor inteiro de 0 a 30: '))
adivinhação=[5,6,10,14,16,20,30]
if chute in adivinhação:
    print('Você acertou um dos númeors que eu estava pensando!')
    if chute > 15:
        print('Esse número é maior do que 20.')
    if chute < 20:
        print('Esse número é menos do que 20.')
    print('Você é fera!!!')
else:
    print('Que pena, você errou! Pode tentar outra vez')
print('Obrigado por participar!')

#CÓDIGO 5
frutas=["maçã","banana","uva","goiaba"]
for x in frutas:
    if x=="uva":
        break
    print(x)

#CÓDIGO 6
n=5
while n>=0:
    n-=1
    print(n)