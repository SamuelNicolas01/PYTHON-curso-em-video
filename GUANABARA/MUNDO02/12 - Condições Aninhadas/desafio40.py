n1 = float(input("Digits a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if n1 < 0 or n1 > 10:
    print(f"Primeira nota inválida {n1}")
elif n2 < 0 or n2 > 10:
    print(f"Segunda nota inválida {n2}")
elif media < 5:
    print(f"Nota: {media}")
    print("REPROVADO")
elif 5 <= media <= 6.9:
    print(f"Nota : {media}")
    print("RECUPERAÇÃO")
else:
    print(f"Nota {media}")
    print("APROVADO")
