# Lista de Exercícios 2
# Tobias Alex - 3INFO3


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


titulo('Exercício 1')
n1 = int(input('Primeiro lado: '))
n2 = int(input('Segundo lado: '))
n3 = int(input('Ultimo lado: '))
if n1 >= 2 and n1 >= n3:
    if n2 + n3 > n1:
        val = True
    else:
        val = False
elif n2 >= n1 and n2 >= n3:
    if n1 + n3 > n2:
        val = True
    else:
        val = False
else:
    if n1 + n2 > n3:
        val = True
    else:
        val = False
if not val:
    print('Não é possível fazer um triângulo.')
else:
    if n1 != n2 != n3 != n1:
        print('É um triângulo \033[31mESCALENO\033[m')
    elif n1 == n2 == n3:
        print('É um triângulo \033[31mEQUILÁTERO\033[m')
    else:
        print('É um triângulo \033[31mISÓCELES')

titulo('Exercício 2')
ano = int(input('Ano a ser verificado: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('É bissexto')
        else:
            print('Não é bissexto')
    else:
        print('É bissexto')
else:
    print('Não é bissexto')

titulo('Exercício 3')
peixes = float(input('Quantos kilos de peixe joão pegou? '))
exesso = 0
multa = 0
if peixes > 50:
    exesso = peixes - 50
    multa = exesso * 4
print(f'João pegou {peixes}kg de peixes passando {exesso}kg do regularmento com uma multa de R${multa:.2f}')

titulo('Exercício 4')
maior = list()
for c in range(1, 4):
    maior.append(input(f'Digite o {c}° número: '))
print(f'O maior número foi {max(maior)}.')

titulo('Exercício 5')
maior = list()
for c in range(1, 4):
    maior.append(input(f'Digite o {c}° número: '))
print(f'O maior número foi {max(maior)} e o menor {min(maior)}.')

titulo('Exercício 6')
bahh = dict()
bahh['Salário bruto'] = float(input('Ganho por hora: R$')) * int(input('Horas por mês: R$'))
print('-=' * 20)
bahh['IR'] = bahh['Salário bruto'] / 100 * 11
bahh['INSS'] = bahh['Salário bruto'] / 100 * 8
bahh['Sindicato'] = bahh['Salário bruto'] / 100 * 5
bahh['Salário Líquido'] = bahh['Salário bruto'] - bahh['IR'] - bahh['INSS'] - bahh['Sindicato']
for k, v in bahh.items():
    print(f'{k}: R${v:.2f}')

titulo('Exercício 7')
m = int(input('Metros quadrados a ser pintados: '))
litros = m / 3
latas = preço = 0
while litros > 0:
    litros -= 18
    latas += 1
    preço += float(80)
print(f'Serão necessárias {latas} latas para pintar a parede, custando R${preço:.2f} em latas de tinta.')
