#1.	Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.
n1 = int(input('Digite a tabuada que você quer calcular: '))
for i in range(1,11):
    multiplicacao = n1*i
    print(f'{n1} X {i} = {multiplicacao}')
