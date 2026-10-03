print("COR DA LETRA\n")

print('\033[30mPRETO')
print('\033[31mVERMELHO')
print('\033[32mVERDE')
print('\033[33mAMARELO')
print('\033[34mAZUL')
print('\033[35mMAGENTA / ROXO')
print('\033[36mCIANO')
print('\033[37mCINZA')

print("\nCOR DE FUNDO\n")

print('\033[40mPRETO')
print('\033[41mVERMELHO')
print('\033[42mVERDE')
print('\033[43mAMARELO')
print('\033[44mAZUL')
print('\033[45mMAGENTA / ROXO')
print('\033[46mCIANO')
print('\033[47mCINZA')

print("\033[m")
print("\nJUNTOS:\n")

print('\033[7;31;44mOlá,mundo')
print("\033[m")

a = int = 3
b = int = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m. A soma é {a + b}')

nome = 'Samuel'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco': '\033[30;107m'
}
print(f"Olá! Muito prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}!!!")