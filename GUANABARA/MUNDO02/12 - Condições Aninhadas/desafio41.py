ano = int(input("Em que ano o Atleta nasceu "))

if ano < 9:
    print("MIRIM")
elif ano > 9 and ano <= 14:
    print("INFANTIL")
elif ano > 14 and ano <= 19:
    print("JUNIOR")
elif ano > 19 and ano <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
