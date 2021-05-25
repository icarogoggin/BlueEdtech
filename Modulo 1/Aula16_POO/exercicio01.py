'''
1)
a - Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
b - Acrescente a classe criada um metodo para mostrar os dados de uma pessoa
c - crie um objeto do tipo pessoa para testar suas propriedades e metodos
'''
class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def imprimir(self):
        print(f'O nome da pessoa é {self.nome} {self.sobrenome} e a idade é {self.idade}')

icaro = pessoa('icaro','Goggin',27)
icaro.imprimir()