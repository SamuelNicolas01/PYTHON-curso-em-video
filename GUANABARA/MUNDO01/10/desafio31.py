viagem = float(input("Qual a distância da viagem? "))

if viagem <= 200:
    cobranca = viagem * 0.50
    print(f"Será cobrado {cobranca:.2f} reais")
else:
    cobranca = viagem * 0.45
    print(f"Será cobrado {cobranca:.2f} reais")
