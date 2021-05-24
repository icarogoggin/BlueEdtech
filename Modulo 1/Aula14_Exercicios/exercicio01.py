#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

   # A soma deles;

   # A multiplicação entre eles;

   # A divisão inteira deles;

   # Mostre na tela qual é o maior;

   # Verifique se o resultado da soma é par ou impar e mostre na tela;

   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
s = n1+n2
m = n1*n2
d = n1//n2
print(':.:.:.:.:CALCULANDO:.:.:.:.:')
print('A soma entre eles é: ',s)
print('A sua multiplicação é: ',m)
print('Sua divisão inteira é:',d)
if n1>n2:
   print('O maior número é o : ',n1)
elif n1==n2:
   print('Os dois são iguais!')
else:
   print('O maior número é o : ',n2)

if s % 2 ==0:
   print('A soma é PAR!')
else:
   print('A soma é IMPAR!')

if m > 40:
   n3 = m/d
   print(f'{m} dividido por {d}: ',n3)
else:
   print('A multiplicação não foi maior que 40!')