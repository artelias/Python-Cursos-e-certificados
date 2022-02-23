#Exercicio 22
nome=str(input('Digite seu nome:')).strip()
print('Seu nome maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print(len(nome)-nome.count(' '))
print(nome.split()[:1])
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 23
numero=int(input('Escolha um numero de 0 a 9999: '))
numeros=str(numero)
print('Unidade {}'.format(numeros[3:4]))
print('Dezena {}'.format(numeros[2:3]))
print('Centena {}'.format(numeros[1:2]))
print('Milhar {}'.format(numeros[0]))

#OU DA FORMA MATEMATICA
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 24
cidade=str(input('Nome da sua cidade natal: ')).strip()
cidadeN=cidade.title()
print((cidadeN[:5])=='Santo')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 25
nome=str(input('Seu nome completo: ')).strip()
nomeC=nome.title()
print('Silva' in nomeC)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')




#Exercicio 26
frase=str(input('Coloque uma frase: ')).strip()
frasen=frase.lower()
print(frasen.count('a'))
print(frase.find('a')+1)
print(frase.rfind('a')+1)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 27
nome=str(input('Seu nome completo: ')).strip()
nomed=nome.split()
print('Seu nome é {}'.format(nome.title()))
print('Seu primeiro nome é {}'.format(nomed[0]))
print('Seu ultimo nome é {}'.format(nomed[len(nomed)-1]))
print('-='*20)