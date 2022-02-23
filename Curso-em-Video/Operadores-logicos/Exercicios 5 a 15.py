#Exercicio 5
n1=int(input('um valor '))
n2=int(input('outro valor '))
print('a soma e {}'.format(n1+n2))
print('n1, o seu sucessor é {} e o antecessor é {} '.format(n1+1,n1-1))
print('n2, o seu sucessor é {} e o antecessor é {} '.format(n2+1,n2-1))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 6
x=int(input('Coloque um número: '))
print('Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(x*2,x*3,x**(1/2)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 7
prova1=float(input('Minha nota foi: '))
prova2=float(input('Minha nota foi: '))
print('Minha média foi {}'.format((prova1+prova2)/2))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 8
parede=int(input('Essa parede tem quantos metros? '))
print('Então ela tem {}cm e {}mm'.format(parede*100,parede*1000))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 9
x=int(input('Coloque um número: '))
i=0
i+=1
print('A tabuada do seu numero é: {} * {} = {}'.format(i,x,i*x))
print(f'A tabuada de 1 desse numero é {x} \na tabuada de 2 desse numero é {x*2} \na tabuada de 3 desse numero é {x*3} '
      f'\na tabuada de 4 desse numero é {x*4} \na tabuada de 5 desse numero é {x*5} \na tabuada de 6 desse número é {x*6} '
      f'\na tabuada de 7 desse número é {x*7} \na tabuada de 8 desse número é {x*8} \na tabuada de 9 desse número é {x*9} '
      f'\na tabuada de 10 desse número é {x*10}')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 10
Carteira=float(input('Quanto de dinheiro você tem? '))
print('Eu tenho {}Reais, mas como vou pro EUA tenho equivalente a {:.2f} dolares'.format(Carteira,Carteira/5.24))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 11
paredea=float(input('Qual alturea da parede? '))
paredel=float(input('Qual a largura da parede? '))
print('Essa parede tem área {} e será necessario {:.2f}L de tinta para pintar'.format(paredea*paredel,(paredea*paredel)/2))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 12
Produto=float(input('O produto vale: '))
print('Mas com desconto de 5% fica {}'.format(Produto*0.95))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 13
rodrigo=float(input('Seu salario é '))
print('parabens pela promoção, seu salario vai ser {}'.format(rodrigo*1.15))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 14
temperatura = float(input('Qual a temperatura da sua cidade: '))
f=((9*temperatura)/5)+32
print('Sua cidade está com temperatuda de {}Cº e {:.1f}Fº'.format(temperatura,f))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 15
dias=int(input('Quantos dias que você alugou o carro?'))
km=int(input('Quantos km você percorreu? '))
aluguel=60*dias
kmR=km*0.15
print('Você alugou o carro por {} dias e andou {}km, Logo você deve pagar R${}'.format(dias,km,aluguel+kmR))
print('-='*20)