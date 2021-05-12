def menor_numero (n1, n2):
    if n1 < n2 :
        print (f'O menor número é o: {n1}')
    else :
        print (f'O menor número é o: {n2}')

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
menor_numero(x, y)