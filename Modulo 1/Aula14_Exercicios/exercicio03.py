
#03 - Utilizando estruturas de repetição com teste lógico,
#  faça um programa que peça uma senha para iniciar seu processamento,
#  só deixe o usuário continuar se a senha estiver correta,
#  após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
#  onde o computador vai “pensar” em um número inteiro entre 0 e 20.
#  O jogador vai tentar adivinhar qual número foi escolhido até acertar,
#  a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
#  no final mostre quantos palpites foram necessários para vencer.
from random import *
senha = '123'
digitesenha = 0
while digitesenha != senha:
    digitesenha = input('Digite sua senha: ')
    if digitesenha != senha:
        print('Senha incorreta! Tente novamente!')
    else:
        break
print("\n" * 10)
print(':.'*30)
print('\t\tBem Vindo ao ADIVINHADOR!')
print(':.'*30)
print()
print('Tente acertar o número que eu pensei! hahaha duvido conseguir!')
numero = randint(0, 20)
jogadas = 0
while True:
    jogadas += 1
    palpite = int(input('Tente acertar o número: '))
    if palpite > numero:
        print('É menor!')
    elif palpite < numero:
        print('É maior!')
    else:
        print(f'Acertou! e você só precisou de {jogadas} jogadas? Eu subestimei você...')
        break

