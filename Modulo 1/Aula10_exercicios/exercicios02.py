'''Exercício 2 - Faça um programa que leia dez conjuntos de dois valores,
 o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
   Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo,
    junto com suas alturas.'''

# pegar o nome do aluno
#pegar altura do aluno
# usar sort para ver o aluno mais alto e mais baixo
# como associar a lista 1 com a lista 2 ? 
idade = []
altura = []
while len(idade) < 2:
  idade_aluno = input('Digite a idade do aluno:  ')
  idade.append(idade_aluno)
  altura_aluno = float(input('Digite a altura do aluno: '))
  altura.append(altura_aluno) 
  altura.sort()
  idade.sort()

print ('O aluno mais novo tem',idade[0],'anos e o aluno mais alto tem', altura[0],'de altura.')

