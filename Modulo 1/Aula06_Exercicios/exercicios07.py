''' 7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
 Se eles forem iguais, imprima que eles são iguais. '''

def comparador(n1, n2):
    maior = 0
    if n1 > n2:
        maior = n1
        print(f'O maior número é: {maior}')
    elif n1 < n2:
        maior = n2
        print(f'O maior número é: {maior}')
    else:
        print('São iguais!')
n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
comparador(n1, n2)