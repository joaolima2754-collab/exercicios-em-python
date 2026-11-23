pares = 0

for i in range(1, 7):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        pares = pares + 1

print("Quantidade de números pares:", pares)