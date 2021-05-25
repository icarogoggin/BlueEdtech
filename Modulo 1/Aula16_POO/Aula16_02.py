class aluno():
    def __init__(self, nome, idade, serie, nota1, nota2, matricula, sala): #o nome do argumento não precisa ser o mesmo do atributo
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.nota1 = nota1
        self.nota2 = nota2
        self.matricula = matricula
        self.sala = sala

    def calcula_media(self):
        self.media = (self.nota1+self.nota2)/2
        print(f'A média do {self.nome} é {self.media}')

    def altera_sala(self):
        nova_sala = input('Digite a nova sala: ')
        confirmacao = input(f'Você quer alterar o aluno {self.nome} de sala?: ')
        if confirmacao == 'S':
            self.sala = nova_sala
        else:
            print('Ok, nada alterado')
        print(f'A sala do(a) aluno(a) {self.nome} é: {self.sala}')

icaro = aluno('icaro',18,'3am',10, 10,'087594', 'sala 15')
nivia = aluno('Nivia', 18, '3am', 9, 5, '1234', 'sala 15')
print(icaro.nome)
icaro.calcula_media()
nivia.calcula_media()
icaro.altera_sala()