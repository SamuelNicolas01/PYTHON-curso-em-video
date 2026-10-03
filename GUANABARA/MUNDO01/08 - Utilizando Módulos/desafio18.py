from math import sin,cos,tan,radians

angulo = float(input("Digite o seu ângulo "))
rad = radians(angulo)

seno = sin(rad)
co = cos(rad)
ta = tan(rad)

print(f"O seu ângulo é igual a {angulo}\n"
      f"seu seno é igual a {seno:.2f}\n"
      f"seu coseno é igual a {co:.2f}\n"
      f"seu tangente é igual a {ta:.2f}")