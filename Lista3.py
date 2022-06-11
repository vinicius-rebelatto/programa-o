from random import randint


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


titulo('Exercício 1')
neg = list()
pos = list()
for c in range(0, 20):
    num = randint(-20, 20)
    if num < 0:
        neg.append(num)
    if num > 0:
        pos.append(num)
print(f'Números negativos ', end='')
for el in neg:
    print(f'{el}', end=' ')
print(f'Média dos positivos deu {sum(pos) / len(pos)}')

titulo('Exercício 2')
for c in range(0, 15):
    num = randint(0, 50)
    print(num, end=' -->  ')
    if num % 2 == 0:
        print('É par')
    else:
        print('É Ímpar')

titulo('Exercício 4')
i = p = 0
for c in range(0, 101):
    if c % 2 == 0:
        p += c
    else:
        i += c
print(f'Os Ímpares foram {i} e os pares {p}')

titulo('Exercício 5')
soma = 0
alturas = [1.50, 1.80, 1.75, 1.79, 1.69, 1.88, 1.65, 1.68, 1.62, 1.55,
           1.43, 1.99, 1.85, 1.82, 1.77, 1.53, 1.75, 1.78, 1.91, 1.67]
for c in alturas:
    soma += c
print(f'A média de alturas foi de {round(soma / len(alturas), 2)}')

titulo('Exercício 6')
n = randint(10, 30)
neg = 0
for c in range(0, n):
    num = randint(-15, 15)
    if num < 0:
        neg += 1
print(f'Dos {n} valores sorteados, {neg} eram negativos')

titulo('Exercício 10')
fat = int(input('De qual número deseja calcular o fatorial? '))
print(f'Fatorial de {fat}', end=': ')
res = 1
for el in range(1, fat + 1):
    res *= el
    if el == fat:
        print(f'{el} = ', end='')
    else:
        print(f'{el} x ', end='')
print(res)

titulo('Exercício 11')
soma = 0
for c in range(1, 101):
    soma += c
print(f'A soma da sequência deu {soma}')
