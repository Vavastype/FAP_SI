wage = int(input("Digite seu valor: "))

if wage > 1000:
  print((5 / 100) * wage)
elif wage > 500 and wage <= 1000:
  print((10 / 100) * wage)
else:
  print((15 / 100) * wage)