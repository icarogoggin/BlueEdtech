'''Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
aos quadrados desses números.

{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81} '''

lista = (1, 4, 5, 6, 7, 9)
fator = {i:i**2 for i in range(1,11)}
print('O resultado é: ',fator)