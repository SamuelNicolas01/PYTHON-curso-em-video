frase = "Curso em Video Python"
print(frase[1:15])

print(frase.upper().count('o')) #quantos "o" tem

print(frase.replace('Curso',"Android")) #substitui palavras

print(len(frase.strip())) #quantas letras tem

print(frase.lower().find('video'))

dividido = frase.split() #cria lista

print(dividido[2][3])

print("Oi\n")
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(, count(), find(), transformações com
replae(), upper), lower(), capitalize(), title(), strip(), junção com join().
""")

print(frase.upper().count('0'))