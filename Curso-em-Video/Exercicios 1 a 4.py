#Exercicio 1
nome = input('Qual seu nome?')
print('Olá', nome, '! Prazer em te conhecer!')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 2
dia = 20
mes = 'jul'
ano = 2000
print('Você nasceu no dia ',dia,'de',mes,'de',ano,'. Correto?')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 3
primeiro=int(input('Primeiro número '))
segundo=int(input('Segundo número '))
soma=primeiro+segundo
print('A soma é: ', soma)
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 4
amostra = input('coloca algo aqui: ')
print('Qual o tipo primitivo dele?', type(amostra))
print('É numerico? ', amostra.isnumeric())
print(f'Só tem espaços? {amostra.isspace()}')
print(f'É alfabético? {amostra.isalpha()}')
print(f'É alfanumérico? {amostra.isalnum()}')
print(f'Está em letras maiúsculas?{amostra.isupper()}')
print(f'Está em letras minúsculas? {amostra.islower()}')
print(f'Está capitalizada? {amostra.istitle()}')
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')