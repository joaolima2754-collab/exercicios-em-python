N = int(input("Digite a quantidade de números (1 a 8): "))

while N < 1 or N > 8:
    print("Quantidade inválida!")
    N = int(input("Digite novamente (1 a 8): "))

soma = 0

for i in range(N):
    numero = float(input("Digite um número: "))
    soma = soma + numero

media = soma / N

print("Soma:", soma)
print("Média:", media)