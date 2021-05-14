'''4.	Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco),
 conte quantas vezes aparece uma vogal.'''
def listavogais(string):
    string = string.lower()
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

print(listavogais('Esta frase é um teste para contar quantas vogais existem aqui.'))