#Exercicio 28
import random
numero=random.randint(0,5)
escolha=int(input('Advinhe um numero: '))
if escolha==numero:
    print('ACERTOU!!!!!')
else:
    print('Errouuuuuuuuuuu!')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 29
velocidade=int(input('O carro estava a quantos KM/H? '))
if velocidade>= 80:
    multa=(velocidade-80)*7
    print('Você foi multado, no valor de R${}'.format(multa))
else:
    print('Tranquilo, continue assim!')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 30
numero=int(input('Escolha um numero '))

if numero%2 == 0 :
    print('Numero par')
else:
    print("impar")
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 31
viagem=int(input('Quantos KM você viajou? '))
if viagem<=200:
    print('Valor a ser pago R${}'.format(0.5*viagem))
else:
    print('valor a ser pago pela viagem longa R${}'.format(0.45*viagem))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 32
ano=int(input('Seu ano?'))
if ano%4==0:
    print('Seu ano é bissexto')
else:
    print('Não é bissexto')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 33
num1=float(input('Escolha um numero: '))
num2=float(input('Escolha um numero: '))
num3=float(input('Escolha um numero: '))
if num1>num2>num3:
    print('o maior é {} e o menor é {}'.format(num1,num3))
else:
    if num2>num3>num1:
        print('o maior é {} e o menor é {}'.format(num2,num1))
    else:
        if num3>num1>num2:
            print('o maior é {} e o menor é {}'.format(num3,num2))
        else:
            if num1>num3>num2:
                print('o maior é {} e o menor é {}'.format(num1,num2))
            else:
                if num2>num1>num3:
                    print('o maior é {} e o menor é {}'.format(num2,num3))
                else:
                    if num3>num2>num1:
                        print('o maior é {} e o menor é {}'.format(num3,num1))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 34
salario=float(input('Seu salario é: '))
if salario>=1250:
    print('Seu salario agora é {:.2f}'.format(salario*1.1))
else:
    print('Seu salario é {:.2f}'.format(salario*1.15))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 35
a=float(input('tamanho: '))
b=float(input('tamanho: '))
c=float(input('tamanho: '))
if a<b+c and b<a+c and c<b+a:
    print('triangulo existe')
else:
    print('não é um triangulo')
print('-='*10)
