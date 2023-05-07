import statistics

'''
15) Faça um programa em Python para encontrar a mediana (o valor médio) de três valores inseridos pelo usuário.

'''

'''

Retorna a mediana (valor do meio) dos dados numéricos.

Quando o número de pontos de dados for ímpar, retorne o ponto de dados do meio. Quando o número de pontos de dados é par, a mediana é interpolada tomando a média dos dois valores do meio:

'''

number_fist = float(input("Digite seu valor: "))
number_second = float(input("Digite seu valor: "))
number_third = float(input("Digite seu valor: "))

number_box = [number_fist, number_second, number_third]

print(statistics.median(number_box))
