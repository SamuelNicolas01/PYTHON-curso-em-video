numero = int(input("Digite um número "))
print("Escolha qual será a base de conversão ")

print(" 1 - Binário \n 2 - Octual \n 3 - Hexadecimal \n")
base = input("Base de conversão : ")

if base == 1:
    print(f"Convertido para Binário é igual a {bin(numero)[2:]}")
elif base == 2:
    print(f"Convertido para Octal é igual a {oct(numero)[2:]}")
elif base == 3:
    print(f"Convertido para Hexadecimal é igual a {hex(numero)[2:]}")
else:
    print("Escreva um valor válido")