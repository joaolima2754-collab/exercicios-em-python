total = 0
deposito = 15

for semana in range(1, 7):
    print(semana, "ª semana: R$", deposito)
    total = total + deposito
    deposito = deposito + 5

print("Total guardado: R$", total)