
#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e 
# conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

def contadorvogais(frase):
    contagem_vogais = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in frase:
            contagem_vogais[i] = frase.count(i)
            frase = frase.replace(i, '')
    print(contagem_vogais)
    print(frase)


frase = input('Digite sua frase aqui: ')
contadorvogais(frase)
