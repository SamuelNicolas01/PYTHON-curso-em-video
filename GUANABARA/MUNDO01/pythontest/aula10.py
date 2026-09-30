nome = str(input("Qual o seu nome? "))

if nome == "Samuel":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal")
print(f"Bom dia, {nome}")

n1 = float(input("Digite sua nota "))
n2 = float(input("Digite sua segunda nota "))
media = (n1 + n2) / 2

print(f"Sua média foi {media}")

if media >= 6:
    print("Sua média foi boa")
else:
    print("Sua média foi ruim")