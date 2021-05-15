senha = 'blabla'
pin = 0
trava_senha = 0
while pin != senha and trava_senha < 3:
    pin = input('Digite sua senha: ')
    if pin != senha:
        print('Senha incorreta! Tente novamente!')
        trava_senha += 1
    else:
        print('Senha Correta! Seja bem vindo!')
