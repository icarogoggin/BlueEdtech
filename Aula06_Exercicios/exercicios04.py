def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    valorhora = float(valor_hora)
    if horas <= 40:
        salario=horas*valorhora
    else:
        h_excd = float(horas - 40)
        salario = float(40*valorhora+(h_excd*(1.5*valorhora)))
    return salario

hora= input('Digite numero de horas: ')
valorHora=input('Digite valor hora: ')
salarioreajustado = calcular_pagamento(hora,valorHora)
print('O valor do salário é:',salarioreajustado,"")