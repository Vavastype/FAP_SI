weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

result = float(weight / (height * height))

if result <= 18.5:
  print("Sou Abaixo do PESO.")
elif result >= 18.5 and result <= 24.9:
  print("Peso saudável")
elif result >= 25 and result <= 30:
  print("Sobrepeso")
elif result >= 30 and result <= 39.9:
  print("Obeso")
else:
  print("Obeso Mórbido")