#Exercicio 57
sexo = str(input('Qual seu sexo? ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Coloque novamente seu sexo: ')).upper()
print('Seu sexo é {}'.format(sexo))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 58
import random
numero=random.randint(0,10)
escolha=int(input('Advinhe um numero: '))
while escolha != numero:
    escolha = int(input('Advinhe um numero novamente: '))
    if escolha==numero:
        print('ACERTOU!!!!!')
    else:
        print('Errouuuuuuuuuuu!')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 59
valor1=int(input('Qual valor você quer?'))
valor2=int(input('Qual valor você quer?'))
print(' ********* MENU ************')
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos números')
print('[5] sair do programa')
print('***************************')
item=int(input('Qual item você quer?'))

while item !=5:
    print(' ********* MENU ************')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    print('***************************')
    item = int(input('Qual item você quer?'))
    if item == 1:
        print('{} + {} = {}'.format(valor1,valor2,valor1+valor2))
    if item == 2:
        print('{} * {} = {}'.format(valor1,valor2,valor1*valor2))
    if item == 3:
        if valor1>valor2:
            print('{} > {}'.format(valor1,valor2))
        else:
            print('{} > {}'.format(valor2,valor1))
    if item == 4:
        valor1 = int(input('Qual valor você quer?'))
        valor2=int(input('Qual valor você quer?'))
    else:
        print('Opção invalida')
print('Encerrando...')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 60
n=int(input('Escolha o numero para transforma em fatorial: '))
c = n
f = 1
while c>0:
    print('{} '.format(c), end='')
    print(' x 'if c>1 else ' = ', end='')
    f *= c
    c-=1
print('{}'.format(f))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 61
p1=int(input('Qual a primeiro termo da pa: '))
razao=int(input('Qual a razão da pa: '))
f=1
g=p1
while f<=10:
    print('{}->'.format(g),end ='')
    g += razao
    f += 1
print('FIM')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 62
print('-=-=-=' * 10)
p1 = int(input('Qual a primeiro termo da pa: '))
razao = int(input('Qual a razão da pa: '))
f = 1
g = p1
mais = 10
total = 0
while mais != 0:
    total += mais
    while f <= total:
        print('{}->'.format(g), end='')
        g += razao
        f += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada com {} termos'.format(total))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')
