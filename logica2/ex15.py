soma = 0

numero = int(input("Digite um número inteiro (0 para encerrar): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro número (0 para encerrar): "))

print("A soma total é:", soma)