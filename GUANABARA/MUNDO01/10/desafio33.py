n1 = int(input("Digite um número "))
n2 = int(input("Digite outro número "))
n3 = int(input("Digite o seu último número "))

if n1 > n2 and n1 > n3:
    print("O primeiro número é o maior!")
elif n2 > n1 and n2 > n3:
    print("O segundo número é o maior")
else:
    print("O terceiro é o maior")