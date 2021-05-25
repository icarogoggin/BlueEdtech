'''Crie uma classe chamada Conta para simular as operações de
uma conta corrente. Sua classe deverá ter os atributos Titular e
Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
Conta e teste os atributos e métodos implementados.'''

class conta():
    def __init__(self, saldo):
        self.saldo = 0

    def transferir(self, saldo):
        self.saldo -= saldo

    def depositar(self, saldo):
        self.saldo += saldo

    def sacar(self, saldo):
        self.saldo += saldo

icaro = conta(0)
continuar = ''
s = 0
print('-='*10)
print('BEM VINDO(A) AO BANCO NO$$O')
print('-='*10)
while continuar != 'sair':
    print('Para transferir uma quantia digite:\t Transferir')
    print('Para depositar uma quantia digite:\t Depositar')
    print('Para sacar uma quantia digite:\t\t Sacar')
    continuar = str(input('Digite uma das opções abaixo ou digite sair para fechar o programa: ')).lower()
    if continuar == 'transferir':
        s = int(input('Quanto você deseja transferir? R$'))
        icaro.transferir(s)
        print (f'Seu saldo atual é de: ',icaro.saldo)
    elif continuar == 'depositar':
        s = int(input('Quanto você deseja depositar? R$'))
        icaro.depositar(s)
        print (f'Seu saldo atual é de: ',icaro.saldo)
    elif continuar == 'sacar':
        s = int(input('Quanto você deseja sacar? R$'))
        icaro.sacar(s)
        print (f'Seu saldo atual é de: ',icaro.saldo)
    else:
        print()
        print('Comando invalido! Escreva uma das opções disponiveis!')
        print()


