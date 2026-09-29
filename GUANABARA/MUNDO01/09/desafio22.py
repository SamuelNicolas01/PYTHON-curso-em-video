nome = str(input("Qual seu nome? ")).strip()
print("como foi escrito : "+nome)

print("nome em maiusculo : " (nome.lower()))
print("nome em minusculo : " (nome.upper()))

print(f"Seu nome possui {len(nome.replace(' ', ''))} letras")

separa = (nome.split())
print(f"seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras ")