contador = 0

for i in range(1, 6):
    idade = int(input("Digite a idade do estudante: "))

    if idade >= 1 and idade <= 120:
        if idade >= 16:
            contador = contador + 1
    else:
        print("Idade inválida!")

print("Quantidade de estudantes com 16 anos ou mais:", contador)