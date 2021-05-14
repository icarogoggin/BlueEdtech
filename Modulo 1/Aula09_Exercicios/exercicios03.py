#3.	O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo: 
#tabuada com o preço do pão e imprimindo de forma diferente

n1 = float(input('Digite a tabuada que você quer calcular: '))
for i in range(1,11):
    multiplicacao = n1*i
    print(f'{n1} X {i} = {multiplicacao}')

#preco = 0.18

#for n in range(1,51,1):
#    print(n,"pães valem R$",n*preco)
