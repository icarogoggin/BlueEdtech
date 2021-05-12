'''Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois
 seja maior que um terceiro parâmetro, chamado limite.'''
def menor_numero (n1, n2):
    limite = 500
    if n1 + n2 > limite :
        print (f'True')
    else :
        print (f'False')

x = int(input('Primeira número: '))
y = int(input('Segundo número: '))
menor_numero(x, y)