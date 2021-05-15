'''2.	Faça um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
 O jogador poderá errar 6 vezes antes de ser enforcado.'''

palavra = 'programar'.upper()
acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra} '
        else:
           mensagem += '_ '
    print(mensagem)
    print('Você já errou: '+ letras_erradas)

    letra = input('Digite a letra: ').upper()

    if letra in palavra:
        print('Você acertou a letra')
        letras_acertadas += letra
        acertos += 1
    else:
        print('Você errou a letra')
        letras_erradas += letra
        erros += 1