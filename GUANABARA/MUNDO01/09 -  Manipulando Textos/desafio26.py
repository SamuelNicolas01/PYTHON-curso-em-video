frase = str(input("Digite uma frase ")).strip().upper()

print(f"A sua frase possui {frase.count("A")} A")
print(f"A posição da primeira letra A é {frase.find("A")+1}")
print(f"A posição da última letra A é {frase.rfind("A")+1}")