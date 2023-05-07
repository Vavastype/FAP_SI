'''
17) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”. OBS: Coloque o critério que desejar.

'''

response = int(5 * (int(input("Status de temperatura: ")) - 32) /9)

if response >= 14:
    print(response,"C° Quente")
elif  response>= 10 and response <= 13:
    print(response,"C° Agradavel.")
else:
    print(response,"C° Frio.")
