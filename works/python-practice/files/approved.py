one_student = int(input("Digite sua nota: "))
two_student = int(input("Digite sua nota: "))

note_student = float((one_student + two_student) / 2)

print(one_student / 2)

if note_student >= 7:
  print("Aprovado.")
elif note_student >= 6:
  print("Tenta buscar melhorar, um pouco mais.")
else:
  print("Reprovado.")
