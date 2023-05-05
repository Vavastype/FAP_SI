alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

alfa_split = alfabeto.split(' ')

for i in alfa_split:
  if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
    print("Vogal")
  else:
    print("consoante")