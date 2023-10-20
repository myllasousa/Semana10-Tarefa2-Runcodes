valor = float(input(""))

for parcelas in range(1, 25):
    prestacao = valor / parcelas
    print(f"{parcelas}x de R$ {prestacao:.2f}")
