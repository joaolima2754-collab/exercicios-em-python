soma = 0

for i in range(1, 5):
    nota = float(input("Digite uma nota de 0 a 10: "))

    if nota >= 0 and nota <= 10:
        soma = soma + nota
    else:
        print("Nota inválida!")

media = soma / 4

print("A média das notas é:", media)