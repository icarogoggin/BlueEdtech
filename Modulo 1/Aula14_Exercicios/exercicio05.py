
#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário 
# e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def contadorvogais(frase):
    contagem_vogais = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in frase:
            contagem_vogais[i] = frase.count(i)
            frase = frase.replace(i, '')
            retirados = sum(contagem_vogais.values())
    print(contagem_vogais)
    print(frase)
    print('A quantidade de letras retiradas é: ', retirados)


frase = input('Digite sua frase aqui: ').lower()
contadorvogais(frase)