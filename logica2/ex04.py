numero = int(input("Digite um número inteiro de 1 a 10: "))

if numero >= 1 and numero <= 10:
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
else:
    print("Número inválido!")