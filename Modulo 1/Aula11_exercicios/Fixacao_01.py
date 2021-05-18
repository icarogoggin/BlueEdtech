'''#criando a lista p o dicionário
lista01 = [('zé', '123-123'), ('joão','234-234'), ('Maria','345-345'), ('Joana','456-456'), ('Pedro','567-567')]
#print(lista01[0])
#print(lista01[0][0])
contatos = dict(lista01)
print(type(contatos))
print(contatos)
nome = input('Digite um nome para pesquisar')
print(contatos.get(nome,'nome não encontrado'))


#dicionário
contatos = {'Pedro':'123-123'}# dicionário é composto por {} e : é como se fosse o = para uma variável
print(contatos)'''


elenco = [('Chris Evans', 'Capitão America'), ('Mark Ruffalo', 'Hulk'), ('Tom Hiddleston', 'Loki'), ('Chris Hemsworth','Thor'), ('Robert Downey Jr', 'Homem de Ferro'), ('Scarlett Johansson','Viúva Negra')]
vingadores = dict(elenco)
nome_ator = input('Digite o nome de um dos atores: ')
print(vingadores.get(nome_ator,'Esse nome não está no elenco!'))
print('O elenco dos vingadores é composto por: ',vingadores)
