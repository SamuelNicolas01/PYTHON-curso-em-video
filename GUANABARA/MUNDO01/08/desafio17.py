from math import hypot

co = float(input("Digite o valor do Cateto Oposto "))
ca = float(input("Digite o valor do Cateto Adjascente "))

hipotenusa = hypot(co,ca) #módulo que calcula a hipotenusa
print(f"{hipotenusa:.2f}")