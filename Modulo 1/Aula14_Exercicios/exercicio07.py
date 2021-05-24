
#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#essa questão me deixou um pouco confuso, no enunciado.

continuar = 7
par = []
impar = []
lista_unica = [par, impar]
while continuar > 0:
    continuar -= 1
    numero = (int(input('Digite o número que você que incluir: ')))
    if numero % 2 ==0:
        par.append(numero)
        par.sort()
    else:
        impar.append(numero)
        impar.sort()
print(lista_unica)
