from math import sqrt


def linha():
    print('\033[41m', end='')
    print('\n\033[m', end='')


def celsius(F=32):
    """
    Transforma Fahrenheit em Célsius
    :param F: °Fahrenheit
    :return: Print do resultado em °C
    """
    C = (F - 32) * 1.8
    print(f'{F}°F em Celsius fica {round(C, 2)}°C')


def hipotenusa(cat1, cat2):
    """
    è realizado o Teorema de Pitágoras
    :param cat1: 1° Cateto
    :param cat2: 2° Cateto
    :return: Print da Hipotenusa
    """
    hipo = sqrt(cat1 ** 2 + cat2 ** 2)
    print(f'Hipotenusa é igual à {hipo}')


def aprovação(nota1, nota2):
    """
    Soma as notas e verifica se o aluno está ou não aprovado
    :param nota1: Primeira nota
    :param nota2: Segunda nota
    :return: Print com a situação do aluno
    """
    media = (nota1 + nota2) / 2
    print(f'Media: {media}')
    if media >= 7:
        print('Situação é igual à aprovado! PARABÉNS!')
    elif media >= 5:
        print('Situação é igual à recuperação! NÃO PERCA O FOCO!')
    else:
        print('Situação ruim, reprovado! Sinto muito, estude mais!')


def polígono(lados, tamanho):
    """
    Calcula a área do polígono e diz qual tipo é
    :param lados: Quantidade de lados do polígono
    :param tamanho: tamanho de um único lado
    :return: Print com o tipo e tamanho do polígono
    """
    tipo = 'SOMENTE OS VALORES 3, 4 E 5 SÃO ACEITOS!'
    if lados == 3:
        tipo = "TRIÂNGULO"
        area = lados * tamanho / 2
    elif lados == 4:
        tipo = 'QUADRADO'
        area = tamanho * tamanho
    elif lados == 5:
        tipo = 'PENTÁGONO'
        area = lados * tamanho / 2
    print(f'O {tipo} tem {area}cm² de área')


def soma(n1, n2):
    print(f'\n{n1} + {n2} = {n1 + n2}')


def sequência(n1, n2):
    """
    Imprime os valores no intervalo
    :param n1: Primeiro termo
    :param n2: Segundo termo
    :return: Printa os valores no intervalo entre os termos
    """
    if n2 < n1:
        n1, n2 = n2, n1
    for c in range(n1, n2):
        print(c, end='  ')
    soma(n1, n2)


def validaNumero():
    while True:
        num = int(input('Digite um número para informar o mês: '))
        if 1 <= num <= 12:
            return num
        else:
            print('\033[31mERRO! Digíte um número válido! [1 à 12]\033[m')


def pegaMês(num):
    """
    Pega o número equivalente ao mês
    :param num: número do mês
    :return: Printa o mês refente ao número.
    """
    meses = ['Janeiro', 'Fevereiro', 'Março',
             'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro']
    print(f'O mês referido {num} equivale à {meses[num-1]}')


celsius(float(input('°F: ')))
linha()
hipotenusa(int(input('Cateto 1: ')), int(input('Cateto 2: ')))
linha()
aprovação(float(input('NOTA 1: ')), float(input('NOTA 2: ')))
linha()
lados = int(input('Quantidade de lados [3, 4 OU 5]: '))
tamanho = int(input('Tamanho de um dos lados [cm]: '))
polígono(lados, tamanho)
linha()
n1 = int(input('Número inteiro para início do intervalo: '))
n2 = int(input('Número inteiro para fim do intervalo: '))
sequência(n1, n2)
linha()
pegaMês(validaNumero())

