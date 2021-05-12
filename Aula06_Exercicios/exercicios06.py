'''6.	Escreva uma função que, dado um número nota representando a nota de um estudante, 
converte o valor de nota para um conceito (A, B, C, D, E e F).'''

def fnota (nota):
    if nota >=9:
        print("SUA NOTA FOI: A")
    elif nota >=8:
        print("SUA NOTA FOI: B")
    elif nota >=7:
        print("SUA NOTA FOI: C")
    elif nota >=6:
        print("SUA NOTA FOI: D")
    elif nota <= 5.9 and nota >= 4.1:
        print("SUA NOTA FOI: E")
    else:
        print("SUA NOTA FOI: F")
### PROGRAMA NOTA EM LETRA ###
nota = float(input('Digite aqui sua nota: '))
fnota(nota)