dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos KM foram percorridos? "))
pagar = (dias * 60) + (km * 0.15)
print(f"Seu carro foi alugado por {dias}, rodou por {km}\n"
      f"por tanto o valor pago será de R$ {pagar:.2f}")