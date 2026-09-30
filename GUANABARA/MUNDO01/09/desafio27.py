from operator import and_

nome = str(input("Digite seu nome completo ")).title().split()

print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome)-1]}")

tempo = int(input("Quantos anos tem seu carro? "))

if tempo >= 10:
    print("Velho")
elif tempo >= 5 and tempo <= 10:
    print("Semi novo")
else:
    print("Novo")
