a = ["Cleide","Joana","Cleber"]
nome = str(input("Qual o seu nome? ")).lower().title()
if nome == "Samuel":
    print("Que nome bonito")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil ")
elif nome in a:
    print("Belo nome feminino")

print(f"Tenha um bom dia, {nome}")