menores = 0
adultos = 0
idosos = 0

for i in range(7):
    idade = int(input("Digite a idade: "))

    if idade < 12:
        menores = menores + 1
    elif idade <= 59:
        adultos = adultos + 1
    else:
        idosos = idosos + 1

print("Menores de 12 anos:", menores)
print("Pessoas de 12 a 59 anos:", adultos)
print("Pessoas com 60 anos ou mais:", idosos)