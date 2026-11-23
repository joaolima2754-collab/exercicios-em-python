numero = int(input("Digite um número inteiro de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Número inválido! Digite outro: "))

print("Número aceito:", numero)