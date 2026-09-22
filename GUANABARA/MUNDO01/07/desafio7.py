n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite sua segunda nota "))

if n1 > 10 or n2 > 10:
    print("Nota inválida")
elif n1 < 0 or n2 < 0:
    print("Nota inválida")
else:
    media = float((n1 + n2) / 2)
    print(f"Média igual a {media}")