quantidade = 0
soma = 0

for i in range(1, 11):
    numero = int(input("Digite um número inteiro: "))

    if numero % 3 == 0 and numero % 5 == 0:
        quantidade = quantidade + 1
        soma = soma + numero

print("Quantidade de números:", quantidade)
print("Soma dos números:", soma)