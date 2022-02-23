#Exercicio 16
numero = float(input('Coloque um numero a sua escolha: '))
print('Esse numero de forma inteiro é {}'.format(int(numero)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')


#Exercicio 17
from gettext import install
import math
CatetoOposto = float(input('Valor do cateto oposto: '))
CatetoAdjacente = float(input('Valor do cateto adjacente: '))
formula=math.sqrt(CatetoOposto**2 +CatetoAdjacente**2)
print('O valor da Hipotenusa é {}'.format(formula))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exemplo 18
import math
an = int(input('Digite um ângulo: '))
sen = math.sin(an)
cos = math.cos(an)
tan = math.tan(an)
print('Sendo assim, o seno é {}, o cosseno é {} e a tangente é {}'.format(round(sen),round(cos),round(tan)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 19
import random
paulo='Paulo'
gustavo='Gustavo'
ana='ana'
bia='bia'
print('{}, {}, {} e {}, o escolhido foi {}'.format(paulo,gustavo,ana,bia,random.sample((paulo,gustavo,ana,bia),1)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 20
import random
paulo='Paulo'
gustavo='Gustavo'
ana='ana'
bia='bia'
print(' sequencia de apresentação é {}'.format(random.sample((paulo,gustavo,ana,bia),4)))
print('-='*10,end='Próximo exercicio')
print('-='*10)
print('\n')



#Exercicio 21
#import pygame 
#pygame.init()
#pygame.mixer.music.load('AC_DC - Highway to Hell')
#pygame.mixer.music.play()
#pygame.event.wait()
#input()
print('-='*20)
