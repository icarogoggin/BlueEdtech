'''Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.'''
def voto(ano_nascimento):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano_nascimento
    if idade <= 15:
        print('NEGADO')
    elif idade >= 16 and idade < 18 :
        print('OPCIONAL')
    else:
        print('OBRIGATORIO')

# programa votação
nascimento = int(input('Em que ano você nasceu?'))
print(voto(nascimento))