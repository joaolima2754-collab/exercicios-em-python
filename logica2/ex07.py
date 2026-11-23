positivos = 0
zeros = 0

for i in range(1, 7):
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        positivos = positivos + 1
    elif numero == 0:
        zeros = zeros + 1

print("Quantidade de números positivos:", positivos)
print("Quantidade de números iguais a zero:", zeros)