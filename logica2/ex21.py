total = 0
quantidade = 0

preco = float(input("Digite o preço do produto (0 para encerrar): "))

while preco > 0:
    total = total + preco
    quantidade = quantidade + 1

    preco = float(input("Digite o preço do produto (0 para encerrar): "))

if quantidade == 0:
    print("Compra vazia")
else:
    print("Total da compra: R$", total)
    print("Quantidade de produtos:", quantidade)