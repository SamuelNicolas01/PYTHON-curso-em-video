r1 = int(input("Qual o r1? "))
r2 = int(input("Qual o r2? "))
r3 = int(input("Qual o r3? "))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print("Da Bom pae, é possível criar um triângulo")
else:
    print("Xi deu ruim, não é possível")