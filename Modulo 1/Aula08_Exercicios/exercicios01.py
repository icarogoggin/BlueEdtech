'''1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a.	tamanho da lista.
b.	maior valor da lista.
c.	menor valor da lista.
d.	soma de todos os elementos da lista.
e.	lista em ordem crescente.
f.	lista em ordem decrescente.'''

L = [5, 7, 2, 9, 4, 1, 3]
print("Lista = ",L)
print("O tamanho da lista é : ",len(L))
print("O maior número da lista é : ",max(L))
print("O menor número da lista é : ",min(L))
print("A soma dos número da lista é : ",sum(L))
L.sort()
print("Lista em ordem crescente: ",L)
L.reverse()
print("Lista em ordem decrescente: ",L)