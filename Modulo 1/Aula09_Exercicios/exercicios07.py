#7.	(DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]
#contador + break
from random import *
numero_da_sorte = randint(0,100)
chances = 10
print(f'\n Tente acertar o número da sorte! você tem {chances} chances para acertar!\n')
while chances > 0:
    chances -= 1
    numero = int(input('Digite o número: '))
    if numero > numero_da_sorte:
        print('O número da sorte é menor!')
        print(f'Você só tem {chances} chances!')
    elif numero < numero_da_sorte:
        print('O número da sorte é maior!')
        print(f'Você só tem {chances} chances!')
    else:
        print(f'Parabéns! Você acertou! O número da sorte é: {numero_da_sorte}!')
        chances = -1
if chances == 0:
    print()
    print('Que pena! Você perdeu!')
    print(f'O número da sorte é {numero_da_sorte}')
    input()
elif chances == -1:
    input()