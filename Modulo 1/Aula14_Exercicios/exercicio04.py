
#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA
# e devolva uma string no formato D de mesPorExtenso de AAAA.
# Valide a data e retorne NULL caso a data seja inválida.


def data_extenso(dia,mes,ano):
    if dia <= 31 and mes <=12:
        meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
        data = str(dia)+' de '+meses[mes]+' de '+str(ano)
        return data
    else:
        data = 'NULL'
        return data

data = data_extenso(23, 5, 2021)
print(data)

