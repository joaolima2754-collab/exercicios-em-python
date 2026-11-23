maior = 0
posicao = 0

for i in range(1, 8):
    numero = int(input("Digite um número inteiro: "))

    if i == 1 or numero > maior:
        maior = numero
        posicao = i

print("Maior número:", maior)
print("Posição da primeira ocorrência:", posicao)