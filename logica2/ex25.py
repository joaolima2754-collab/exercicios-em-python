quantidade = 0
maior = 0

numero = int(input("Digite um número positivo (0 para encerrar): "))

while numero != 0:

    if numero < 0:
        print("Número inválido! Digite outro.")

    else:
        quantidade = quantidade + 1

        if quantidade == 1 or numero > maior:
            maior = numero

    numero = int(input("Digite um número positivo (0 para encerrar): "))

if quantidade == 0:
    print("Nenhum número válido foi digitado.")

else:
    print("Quantidade de números válidos:", quantidade)
    print("Maior número:", maior)