'''

24) Um vendedor recebe um determinado valor de comissão sobre o total de suas vendas efetuadas. Em vendas superiores a 5000,00 o valor a
receber corresponde a 25%, os valores na faixa de 5000,00 a 2500,00 corresponde a 20% e para valores inferiores a 2500,00 o valor corresponde a 15%.
Implemente um programa que leia o valor total das vendas (número real) e calcule a quantia que o vendedor irá receber

'''

commission = float(input("Digite seu valor de vendas: "))

if commission > 5000:
    print(commission + (commission * (25 / 100))," Valor total com a comissão")
elif commission >= 2500 and commission <= 5000:
    print(commission + (commission * (20 / 100))," Valor total com a comissão")
else:
    print(commission + (commission * (15 / 100))," Valor total com a comissão")