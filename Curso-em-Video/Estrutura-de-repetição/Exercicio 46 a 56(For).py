#Exercicio 46
for c in range(10,0,-1):
    print(c)
print('puff')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 47
for c in range(1,51):
    if c%2==0:
        print(c)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 48
s = 0
for c in range(1,501,2):
    if c%3==0:
        s = s+c
print(s)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 49
numero=int(input('Escolha um numero da tabuada: '))
for c in range(1,11):
    tabuada=numero * c
    print('{} * {} = {}'.format(numero,c,tabuada))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 50
s = 0
for c in range(0,7):
    if c%2==0:
      s=c+s
print(s)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 51
p1=int(input('Qual a primeiro termo da pa: '))
razao=int(input('Qual a razão da pa: '))
decimo=p1+(10-1)*razao
for c in range(p1,decimo+razao,razao):
    print(c,end='->')
print('acabou')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 52
num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 53
frase=input('Qual frase você quer? ').strip().upper()
palavra=frase.split()
junto=''.join(palavra)
inverso= ''
for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print(junto, inverso)
if inverso== junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 54
atual=2022
totalmaior=0
totalmenor=0
for pessoas in range(1,8):
    pessoa = int(input('Ano de nascimento: '))
    idade=atual-pessoa
    if pessoa<=2004:
        totalmaior+=1
    else:
        totalmenor+=1

print('Temos {} pessoas maiores de idade'.format(totalmaior))
print('Temos {} pessoas menor de idade'.format(totalmenor))

print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')





#Exercicio 55
maior = 0
menor = 99999999
for p in range(1, 6):
    peso = float(input('peso da {}º pessoa '.format(p)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 56
somaidade = 0
maioridadedehomem = 0
nomevelho = ''
menoridade=0
for n in range(1, 5):
    print('---- {}º PESSOA ------'.format(n))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if n == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade<20:
        menoridade +=1
mediaidade = somaidade/4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem  mais velho tem {} e seu nome é {}'.format(maioridadedehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menoridade))

print('-='*10)
print('\n')
