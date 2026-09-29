nome = str(input("Qual seu nome completo? ")).strip()
nom = "SILVA" in nome.upper()
print(f"Seu nome tem Silva? {nom} ")

if nom == True: (
    print("Seu nome tem silva")
)
else:
    print("Não tem")