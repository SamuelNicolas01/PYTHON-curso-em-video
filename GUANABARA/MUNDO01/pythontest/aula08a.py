#importa todas as funções do módulo/biblioteca math
import math

#se faz necessário colocar o.math antes de usar a função
num = int(input("Digite um número "))
raiz = math.sqrt(num) #math.sqrt() calcula a raiz quadrada
print(f"A raiz de {num} é igual a {raiz:.2f}\n")
#math.ceil(raiz) arredonda para cima!
#math.floor(raiz) arredonda para baixo!

#para importar funções expecificas de math
from math import sqrt,floor

#não é necessário colocar o .math
num = int(input("Digite um número "))
raiz = sqrt(num) #math.sqrt() calcula a raiz quadrada
print(f"A raiz de {num}, arredonda por floor é igual a {floor(raiz):.2f}\n")

#biblioteca/módulo que gera um número aletatório
import random

num = random.randint(1,10)
print(f"Número aleatório importado por 'random' {num}\n")

import emoji
print(emoji.emojize("Olá mundo :sunglasses:"))