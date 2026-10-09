idade = int(input("Qual a sua idade? "))

if idade <= 0:
    print("Digite uma idade válida!")
else:
    if idade == 18:
        print("Está no tempo de se Alistar!")
    elif idade < 18:
        alistamento = 18 - idade
        print(f"Faltam {alistamento} anos para você se alistar")
    else:
        alistamento = idade - 18
        print(f"Você está {alistamento} anos atrasado!")

print("FIM")