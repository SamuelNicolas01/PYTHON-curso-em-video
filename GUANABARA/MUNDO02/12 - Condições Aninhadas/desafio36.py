valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Em quantos anos o comprador ira pagar? "))
quantidade = 12 * anos
prestacao = float(valor / (12 * anos))

if prestacao >= (0.30 * salario):
    print("Negado")
else:
    print(f"Aprovado , suas pretacoes serão de {prestacao:.2f} e foi dividida em {quantidade} vezes ")

print("Fim")