'''
18) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.

Fórmulas:

De Fahrenheit para Celsius:
celsius = int(5*(fahrenheit -32)/9

De Celsius para Fahrenheit:
Fahrenheit = int((celsius / 5) * 9 + 32)

Valores testes:

95 ºF = 35 ºC

50 ºF = 10 ºC

14 ºF = -10 ºC

'''

transform = int(input(
    "Conversor: 1° para Fahrenheit e 2° para Celsius digite: "
))

if transform == 1:
    response = int((int(input("Digite seu valor em Celsius: ")) / 5) * 9 + 32)
    print(response,"°F - Fahrenheit.")
elif transform == 2:
    response = int(5 * (int(input("Digite seu valor em Celsius: ")) - 32) / 9)
    print(response,"°C - Celsius.")
else:
    print("Por favor digite uma opção valida. 1° para Fahrenheit e 2° para Celsius")