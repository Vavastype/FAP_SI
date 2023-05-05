one_number = int(input("Digite primeiro operador: "))
symbol_operation = input("Digite seu operador: ")
two_number = int(input("Digite segundo operador: "))

if symbol_operation == "+":
  print(one_number + two_number)
elif symbol_operation == "-":
  print(one_number - two_number)
elif symbol_operation == "*":
  print(one_number * two_number)
elif symbol_operation == "/":
  print(one_number / two_number)
else:
  print("Por favor, digite um operador valido ( +, -, *, /).")