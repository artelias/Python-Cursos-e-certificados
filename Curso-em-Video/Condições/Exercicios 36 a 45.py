#Exercicio 36
salario=float(input('Quanto você recebe? '))
casa=float(input('Qual o valor da casa? '))
anos=int(input('Com quantos anos você pretende pagar? '))
prestacoes=anos*12
valor=casa/prestacoes
if valor<=0.3*salario:
    print('Seu credito foi aprovado!!')
    print('Você irá pagar {:.2f} durante {} por mes'.format(valor,prestacoes))
else:
    print('Infelizmente você não pode financiar a casa!!')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 37
import random
numero=random.randint(0,999)
numerointeiro=int(input('Qual numero você quer(1,2,3)? '))
if numerointeiro==1:
    print(bin(numero)[2::])
elif numerointeiro==2:
    print(oct(numero)[2::])
else:
    print(hex(numero)[2::])
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 38
alistamento=int(input('Ano de nascimento '))
if alistamento > 2004:
    print('Ta novinho ainda, fique tranquilo!')
    print('Falta {} anos pra tu mané'.format((alistamento+18)-2022))
elif alistamento ==2004:
    print('Se fudeu, vai pro exercicito menor')
else:
    print('ta veio pcr')
    print('teu alistamento foi {}'.format(2022-(alistamento+18)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 39
nota1=float(input('Qual sua nota?'))
nota2=float(input('Qual sua nota?'))
nota3=float(input('Qual sua nota?'))
media=(nota1+nota2+nota3)/3
if media<5:
    print('REPROVADO, tu é mt burro')
elif media>=5 and media<=6.9:
    print('Vai pra recuperação')
else:
    print('PARABÉNS, ta aprovado')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')





#Exercicio 40
nascimento=int(input('Ano de nascimento '))
if nascimento > 2013:
    print('Sua categoria é mirim!')
elif nascimento >=2008:
    print('Sua categoria é infantil')
else:
    if nascimento >=2003:
        print('Sua categoria é junior')
    else:
        print('Sua categoria é master')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 41
a=float(input('tamanho: '))
b=float(input('tamanho: '))
c=float(input('tamanho: '))
if a<b+c and b<a+c and c<b+a:
    print('triangulo existe')
    if a==b==c:
        print('Triangulo equilátero')
    elif a==b or b==c or a==c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('não é um triangulo')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 43
peso=float(input('Quanto você pesa? '))
altura=float(input('Quanto você tem de altura? '))
imc=peso/(altura**2)
if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideal')
else:
    if imc>=25 and imc<30:
        print('Sobrepeso')
    elif imc>=30 and imc<40:
        print('Obsidade')
    else:
        print('Obesidade mórbida')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 44
produto=float(input('Qual o preço do produto? '))
condicao=str(input('Como você vai pagar?')).upper()
if condicao == 'DINHEIRO':
    print('Você deve pagar R${}'.format(produto*0.9))
elif condicao == 'CARTÃO':
    print('Você deve pagar R${}'.format(produto*0.95))
else:
    if condicao == '2X NO CARTÃO':
        print('Você deve pagar R${}'.format(produto))
    else:
        print('Você deve pagar R${}'.format(produto * 1.2))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 45
import random
maquina=random.random('PEDRA','PAPEL','TESSOURA')
escolha=str(input('qual você escolhe? ')).upper()
if maquina == escolha:
    print('empate')
elif maquina == 'PEDRA' and escolha == 'PAPEL':
    print('Você ganhou')
elif maquina == 'PAPEL' and escolha == 'PEDRA':
    print('Você perdeu')
elif maquina == 'PEDRA' and escolha == 'TESSOURA':
    print('você perdeu')
elif maquina == 'TESSOURA' and escolha == 'PEDRA':
    print('Você ganhou')
elif maquina == 'TESSOURA' and escolha == 'PAPEL':
    print('você perdeu')
elif maquina == 'TESSOURA' and escolha == 'PEDRA':
    print('Você ganhou')
print('-='*10)


