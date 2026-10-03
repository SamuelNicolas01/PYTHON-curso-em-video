vel = float(input("Digite a velocidade do Carro "))
if vel > 80:
    km = float(input("Quantos KM você percorreu? "))
    multa = km * 7
    print(f"Você está multado!, você estava à {vel}/h")
    print(f"A multa será de {multa}")
else:
    print("Ta suáve")