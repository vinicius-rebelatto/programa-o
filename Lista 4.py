from random import randint, random


def titulo(msg):
    print()
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


titulo('Exercício 1')
vet = []
for c in range(0, 100):
    vet.append(c)
print(vet)

titulo('Exercício 2')
vet.clear()
for c in range(0, 10):
    vet.append(randint(0, 10))
print(vet)

titulo('Exercício 3')
vet.clear()
print('Os valores acima da média :')
for c in range(0, 10):
    num = randint(0, 10)
    vet.append(num)
media = sum(vet) / len(vet)
for c in vet:
    if c >= media:
        print(f'{c}', end=' ')

titulo('Exercício 4')
vet.clear()
men = mai = soma = 0
for c in range(0, 30):
    vet.append(randint(0, 10))
for e, c in enumerate(vet):
    if e == 0:
        men = mai = c
    elif mai < c:
        mai = c
    elif men > c:
        men = c
print(f'A maior nota foi {mai} e a menor {men}')
media = sum(vet) / len(vet)
print('Os valores abaixo da média: ')
for c in vet:
    if c <= media:
        print(f'{c}', end=' ')

titulo('Exercício 5')
vet.clear()
for c in range(0, 100):
    vet.append(randint(0, 50))
pos = []
for e, el in enumerate(vet):
    if el == 30:
        pos.append(e)
print(f'As posições em que se encontra o número 30 foram: ')
print(pos)
for c in pos:
    print(vet[c], end=' ')

titulo('Exercício 7')
vet.clear()
for c in range(0, 200):
    vet.append(randint(0, 100) + round(random().real, 2))
print(f'Ordem certa: {vet}')
print(f'Ordem contrária: {vet[::-1]}')

titulo('Exercício 8')
vet.clear()
vet2 = []
vet3 = []
for c in range(0, 20):
    vet.append(randint(0, 9))
    vet2.append(randint(0, 9))
    vet3.append(vet[c] + vet2[c])
print('Vetor 1: ', end='')
for c in vet:
    print(f'{c:<4}', end='')
print('\nVetor 2: ', end='')
for c in vet2:
    print(f'{c:<4}', end='')
print('\nVetor 3: ', end='')
for c in vet3:
    print(f'{c:<4}', end='')

titulo('Exercício 9')
vet.clear()
vet2.clear()
vet3.clear()
for c in range(0, 25):
    vet.append(randint(0, 9))
    vet2.append(randint(0, 9))
for c in range(0, 25):
    vet3.append(vet[c])
    vet3.append(vet2[c])
print(f'Vetor 1: {vet}')
print(f'Vetor 2: {vet2}')
print(f'Vetor composto: {vet3}')

titulo('Exercício 12')
vet.clear()
A = []
for c in range(0, 20):
    A.append(randint(0, 9))
desce = 19
sobe = res = 0
while desce > 9:
    res += (A[sobe] - A[desce]) ** 2
    desce -= 1
    sobe += 1
print(res)

titulo('Exercício 15')
vet.clear()
for c in range(0, 20):
    vet.append(randint(0, 9))
vet.sort()
print(vet)
