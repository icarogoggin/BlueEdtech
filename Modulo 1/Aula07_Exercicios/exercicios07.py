'''PROJETO: Gastos com viagem -  Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
Hospedagem'''

'''1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
Passagem '''
def custo_hotel(noites):
    diaria = 140
    custo_do_hotel = noites * diaria
    print ('O custo do hotel será de : R$',custo_do_hotel)
    return custo_do_hotel
#teste = int(input('Digite quantos dias você pretende ficar no hotel:  '))
#custo_hotel(teste)
'''2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.
Aluguel de Carro'''

def custo_aviao(cidade):
    custoaviao = 0
    if cidade == 'São Paulo':
        custoaviao = 312
        print('O seu custo com a passagem de avião será de : R$',custoaviao)
    elif cidade == 'Porto Alegre':
        custoaviao = 447
        print('O seu custo com a passagem de avião será de : R$',custoaviao)
    elif cidade == 'Recife':
        custoaviao = 831
        print('O seu custo com a passagem de avião será de : R$',custoaviao)
    elif cidade == 'Manaus':
        custoaviao = 986
        print('O seu custo com a passagem de avião será de : R$',custoaviao)
    else:
        print('Você não digitou um destino válido! Tente novamente')
    return custoaviao
#teste = input('Digite o nome da cidade que você vai viajar: ')
#custo_aviao(teste)
'''3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.
Cálculo Total'''
def custo_carro(dias):
    if dias >= 3 and dias < 7:
        aluguel_carro = dias * 40 - 20
        print ('O custo com o aluguel do carro será de : R$',aluguel_carro)
    elif dias >= 7:
        aluguel_carro = dias * 40 - 50
        print ('O custo com o aluguel do carro será de : R$',aluguel_carro)
    else:
        aluguel_carro = dias * 40
        print ('O custo com o aluguel do carro será de : R$',aluguel_carro)
    return aluguel_carro

# teste = int(input('Você pretende alugar o carro por quantos dias : '))
# custo_carro(teste)

'''4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!
Gastos Extras'''

def calcular_viagem(cidade, dias):
    aviao = custo_aviao(cidade)
    hotel =custo_hotel(dias)
    carro =custo_carro(dias)
    total = aviao + hotel + carro
    print(f'O custo total de sua viagem será de: R$',total)


# cidade = input('Digite o nome da cidade que você vai viajar: ').capitalize()
# dias = int(input('Você pretende ficar por quantos dias : '))
# calcular_viagem(cidade, dias)


'''5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.'''
def calcular_viagem_custo(cidade, dias):
    print(f'Seus custos para viajar para a cidade de {cidade} durante {dias} dias, serão: \n')
    custo_extra = 800 #float(input('Você planeja levar algum dinheiro para emergencias? digite a quantia! R$:'))
    aviao = custo_aviao(cidade)
    hotel =custo_hotel(dias)
    carro =custo_carro(dias)
    print(f'Seu custo extra será de: R${custo_extra}')
    total = aviao + hotel + carro + custo_extra
    print(f'O custo total de sua viagem será de: R$',total)

calcular_viagem_custo("Manaus", 12)