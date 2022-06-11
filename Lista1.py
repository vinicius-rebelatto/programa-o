# Lista de exercícios 1
# Tobias Alex - 3INFO3


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


titulo('Exercício 1')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print(f'{n1} + {n2} = {n1 + n2}')

titulo('Exercício 2')
metro = int(input('Valor em metros a ser convertido em milímetros: '))
res = metro * 1000
print(f'{metro} metro em milímetros fica {res} milímetros')

titulo('Exercício 3')
dia = int(input('Dias: ')) * 86400
hora = int(input('Horas: ')) * 3600
min = int(input('Minutos: ')) * 60
seg = int(input('Segundos: ')) + dia + hora + min
print(f'o tempo total em segundos é {seg}')

titulo('Exercício 4')
sal = float(input('Salário a ser aumentado: R$'))
por = int(input('Porcentagem de aumento: '))
res = sal + (sal / 100 * por)
print(f'R${sal:.2f} aumentado em {por}% ficou R${res:.2f}')

titulo('Exercício 5')
sal = float(input('Preço da mercadoria: R$'))
por = int(input('Porcentagem de desconto: '))
res = sal - (sal / 100 * por)
print(f'R${sal:.2f} com {por}% de desconto ficou R${res:.2f}')

titulo('Exercício 6')
dis = int(input('Distancia a percorrer (Km): '))
vel = int(input('Velocidade média (km/h): '))
res = dis / vel
print(f'Percorrer {dis}Km à {vel}Km/h leva {res} horas de viagem.')

titulo('Exercício 7')
c = float(input('Temperatura (C°): '))
f = c * 1.8 + 32
print(f'{c}°C em Firenheite fica {f}°F')

titulo('Exercício 8')
f = float(input('Temperatura (F°): '))
c = (f - 32) / 1.8
print(f'{f}°F em Celsius fica {c:.1f}°C')

titulo('Exercício 9')
km = float(input('Kilometros percorridos: '))
dias = float(input('Dias alugados: '))
res = km * 0.15 + dias * 60
print(f'Após rodar {km}Km em {int(dias)} dia, a tarifa à pagar é R${res:.2f}.')

titulo('Exercício 10')
cigarroDia = int(input('Cigarros fumados por dia: '))
anosFumando = int(input('Anos fumando: '))
tot_cigarro = cigarroDia * 365 * anosFumando * 10
tempo = tot_cigarro / 6 / 24
print(f'Baseado na quantidade de cigarros fumados sua vida foi encurtada em {int(tempo)} dia')

titulo('Exercício 11')
num = str(2**1000000)
tot = len(num)
print(f'2 elevado a um milhão equivale a {tot} dígitos.')
