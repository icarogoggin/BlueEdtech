def somaImposto(taxaImposto, custo):
    taxaImposto_float = float(taxaImposto)/100
    custo_reajustado = custo + (custo * taxaImposto_float)
    print(f'O valor do custo com taxa do imposto é {custo_reajustado:.2f}')

### Programa Calculadora de Imposto ###
custo = float(input("Valor do Produto = R$ "))
taxaImposto = input("Taxa do imposto = ").replace("%","")
somaImposto(taxaImposto, custo)