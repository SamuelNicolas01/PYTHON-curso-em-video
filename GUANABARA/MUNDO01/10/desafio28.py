import random

numero = random.randint(0,5)
print("Estou pensando em um número entre 0 e 5")
n = int(input("Digite seu palpite "))

if n == numero:
    print(f"Parabéns você acertou! O número era {numero}")
else:
    print("Errou!")

