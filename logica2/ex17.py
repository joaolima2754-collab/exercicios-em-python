soma = 0
aprovadas = 0

for i in range(5):
    nota = float(input("Digite uma nota de 0 a 10: "))

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite novamente.")
        nota = float(input("Digite uma nota de 0 a 10: "))

    soma = soma + nota

    if nota >= 6:
        aprovadas = aprovadas + 1

media = soma / 5

print("Média:", media)
print("Notas maiores ou iguais a 6:", aprovadas)