soma = 0
quantidade = 0

temperatura = float(input("Digite a temperatura (999 para encerrar): "))

while temperatura != 999:
    soma = soma + temperatura
    quantidade = quantidade + 1

    temperatura = float(input("Digite a temperatura (999 para encerrar): "))

if quantidade == 0:
    print("Nenhum registro")
else:
    media = soma / quantidade
    print("Quantidade de registros:", quantidade)
    print("Média das temperaturas:", media)