'''6.	Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.'''

frase = input('Digite aqui sua frase: ')
exclusao = 'aeiou'

for i in exclusao:
    frase = frase.replace(i, '')
    
print(frase)