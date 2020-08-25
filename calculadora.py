import math
import os
print('Olá, sou uma mini inteligência que faz cauculos para você!!')
print('''Eu consigo fazer varios tipos de cauculos para você! Vamos la! Vou te dar as opções!''')
desejo = int(input('''
    01-Teorema de Pitagoras
    02-Descobrir SENO, COSSENO e TANGENTE
    03-Descobrir o volume
    Digite a opção desejada: '''))

if desejo == 1:
    print('''    Você escolheu o Teorema de Pitagoras!
    Agora digita qual a forma que devo calcular!''')
    pita = int(input('''    01-Calcular a HIPOTENUSA a partir do CATETO 1 e 2
    02-Calcular o CATETO a partir da HIPOTENUZA e do outro CATETO
    Digite a opção desejada: '''))
    if pita == 1:
        print('    01-Calcular a HIPOTENUSA a partir do CATETO 1 e 2')
        cateto1 = float(input('       Qual o valor do CATETO 1? '))
        cateto2 = float(input('       Qual o valor do CATETO 2? '))
        hipo = cateto1**2 + cateto2**2
        hipofinal = math.sqrt(hipo)
        print('      O valor da HIPOTENUZA do seu triângulo é {:.2f}' .format(hipofinal))
    if pita == 2:
        print('    02-Calcular o CATETO a partir da HIPOTENUZA e do outro CATETO')
        cateto1 = int(input('       Qual o valor do CATETO? '))
        hipo = int(input('       Qual o valor do HIPOTENUZA? '))
        cateto2 = hipo**2 -cateto1**2
        hipofinal = math.sqrt(cateto2)
        print('       O valor do CATETO do seu triângulo é {:.2f}' .format(hipofinal))
if desejo == 2:
    print('   Você escolheu descobrir SENO, COSSENO e TANGENTE!')
    x = float(input('       Digite o valor do angulo: '))
    xradian = math.radians(x)
    cosdex = math.cos(xradian)
    sendex = math.sin(xradian)
    tandex = math.tan(xradian)
    print('       Aqui esta o valor de seno, cosseno e da tangente do ângulo {}'.format(x))
    print('       SENO: {:.2f}'.format(sendex))
    print('       COSSENO: {:.2f}'.format(cosdex))
    print('       TANGENTE: {:.2f}'.format(tandex))
if desejo == 3:
    volu = int(input('''
    01-Calcular o VOLUME de um CILINDRO
    02-Calcular o VOLUME de um CONE
    03-Calcular o VOLUME de um RETANGULO ou QUADRADO
    04-Calcular o VOLUME de uma ESFERA
    05-Calcular o VOLUME de uma PIRAMIDE
    Digite a opção desejada: '''))
    if volu == 1:
        print('    01-Calcular o VOLUME de um CILINDRO')
        raio = float(input('      Digite o valor do raio: '))
        altu = float(input('       Digite o valor da altura: '))
        print('       Para calcular o resultado será utilizado PI = 3,14')
        A = float(raio**2 * 3.14)
        vol = float(A * altu)
        print('       O volume desse objeto é igual a {:.2f}³'.format(vol))
    if volu == 2:
        print('    02-Calcular o VOLUME de um CONE')
        raio = float(input('      Digite o valor do raio: '))
        altu = float(input('      Digite o valor da altura: '))
        print('       Para calcular o resultado será utilizado PI = 3,14')
        base = 3.14 * raio**2
        vol = float(1/3 * (base * altu))
        print('       O volume desse objeto é igual a {:.2f}³'.format(vol))
    if volu == 3:
        print('    03-Calcular o VOLUME de um RETANGULO ou QUADRADO')
        comp = float(input('       Digite o valor do comprimento: '))
        larg = float(input('       Digite o valor da largura: '))
        altu = float(input('       Digite o valor da altura: '))
        vol = float(comp * larg * altu)
        print('       O volume desse objeto é igual a {:.2f}³'.format(vol))
    if volu == 4:
        print('    04-Calcular o VOLUME de uma ESFERA')
        raio = float(input('       Digite o raio: '))
        vol = float(4/3 * 3.14 * raio**3)
        print('       Para calcular o resultado será utilizado PI = 3,14')
        print('       O volume desse objeto é igual a {:.2f}³'.format(vol))
    if volu == 5:
        print('    05-Calcular o VOLUME de uma PIRAMIDE')
        larg = float(input('       Digite o valor da largura: '))
        altu = float(input('       Digite o valor da altura: '))
        base = float(larg ** 2)
        vol = float(1/3 * (base * altu))
        print('       O volume desse objeto é igual a {:.2f}³'.format(vol))

sair = int(input('Digite 1 para voltar ao início ou 0 para sair.'))

if sair == 1:
    os.startfile('APP.exe')
else:
    print('saindo...')
    print(' ')