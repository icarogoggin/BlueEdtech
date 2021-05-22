def faz_tudo():
    num1 = float(input('Digite num1: '))
    num2 = float(input('Digite num2: '))
    if num1 > num2:
        print(f'O número {num1} é maior')
    elif num1 < num2:
        print(f'O número {num2} é maior')
    else:
        print(f'O número {num1} é igual ao {num2} são iguais.')
    soma = num1 + num2
    print(soma)

faz_tudo()