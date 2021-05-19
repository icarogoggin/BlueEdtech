'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
contribuir por 35 anos para se aposentar.'''

#pegar dados, nome, nasc, calcular idade
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['sexo'] = input('M/F: ').upper()
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    if dados['sexo'] == 'M':
        dados['contratação'] = int(input('Ano de Contratação: '))
        dados['salário'] = int(input('Salário: R$'))
        dados['aposentadoria'] = dados['idade']+((dados['contratação'] + 35) - datetime.now().year)
    elif dados['sexo'] == 'F':
        dados['contratação'] = int(input('Ano de Contratação: '))
        dados['salário'] = int(input('Salário: R$'))
        dados['aposentadoria'] = dados['idade']+((dados['contratação'] + 30) - datetime.now().year)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')