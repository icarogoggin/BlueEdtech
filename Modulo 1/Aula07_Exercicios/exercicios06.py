'''Exercício 6 
Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
'''

def boletim(n1, n2, n3):
    maior = n1
    meio = n1
    menor = n1
    if n2 > maior: #Selecionar qual é a maior nota
        maior = n2
    elif n3 > maior:
        maior = n3
    if maior >= n2 > n3: #Selecionar a nota do meio
        meio = n2
    elif maior >= n3 > n2:
        meio = n3
    elif maior >= n1 > n2:
        meio = n1
    if n2 < menor: #Selecionar a menor nota
        menor = n2
    if n3 < menor:
        menor = n3
    media_tres_notas = (n1 + n2 + n3)/3
    media_notas_alta = (maior+meio) / 2
    print(f'Média com as três notas: {media_tres_notas:.2f}')
    print(f'Médias com duas melhores notas: {media_notas_alta}')
    print(f'Sua nota mais alta: {maior}')
    print(f'Sua nota mais baixa: {menor}')


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
boletim(nota1, nota2, nota3)