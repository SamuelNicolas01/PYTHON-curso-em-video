salario = float(input("Digite o valor do seu salário "))

if salario > 1250:
    aumento = (salario * 0.10)
    salario = aumento + salario
    print(f"Com o seu aumento seu salario passa a ser de {salario:.2f}")
else:
    aumento = (salario * 0.15)
    salario = aumento + salario
    print(f"Com o seu aumento seu salario passa a ser de {salario:.2f}")
