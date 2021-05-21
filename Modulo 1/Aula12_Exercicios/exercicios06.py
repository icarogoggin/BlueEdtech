'''DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.'''

todos = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    while True:
        pessoa['sexo'] = input(' Sexo: (M/F): ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    todos.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? (S/N): ').upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp =='N':
        break
print('=*30')
print(f'Ao todo temos {len(todos)} pessoas cadastradas.')
média = soma / len(todos)
print(f'A média de idade é de {média:.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in todos:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in todos:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('== ENCERRADO ==')