'''Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
#nome do jogador
#qts gols
jogador = []
gols = []

def ficha ():
    nome_jogador = input('Digite o nome do jogador: ')
    jogador.append(nome_jogador)
    qtd_gols = input('Digite a quantidade de gols marcados: ')
    gols.append(qtd_gols)

ficha()
print(f'O jogador',jogador[0], 'fez', gols[0], 'gols até o momento em sua carreira!')