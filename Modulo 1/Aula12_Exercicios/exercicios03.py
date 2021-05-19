'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
reprovado.'''

alunos = dict() #aqui criei o dicionário dos alunos
alunos['nome'] = str(input('Nome: ')) #colocar input pra inserir nome dos alunos
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] > 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado' 
for a, b in alunos.items():
    print(f' -- {a} é igual a {b}')