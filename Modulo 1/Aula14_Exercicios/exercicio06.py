
#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

respostas = []
respostas.append(input("Telefonou para a vítima? Sim ou Não: "))
respostas.append(input("Esteve no local do crime? Sim ou Não: "))
respostas.append(input("Mora perto da vítima? Sim ou Não: "))
respostas.append(input("Devia para a vítima? Sim ou Não: "))
respostas.append(input("Já trabalhou com a vítima? Sim ou Não: "))
respostas_sim = respostas.count('Sim')
if (respostas_sim < 2):
    print("Inocente")
elif (respostas_sim == 2):
    print("Suspeito")
elif (3 <= respostas_sim <= 4):
    print("Cúmplice")
else:
    print("Assassino")

