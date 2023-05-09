'''
23) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

'''

price_home = float(input("Digite o valor de sua casa: "))
salary = float(input("Digite o valor mensal de salario: "))
years_price = float(input("Quantidade de parcelas: "))

provision = (price_home / years_price) + 3
print(provision)
limit_salary = (30 / 100) * price_home

if provision < limit_salary:
    print(provision)
else:
    print("Desculpe seu saldo não bate.")
