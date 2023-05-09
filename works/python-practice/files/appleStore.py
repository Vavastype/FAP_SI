'''

20) Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra. Considere que as maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze.

'''

account_apple = int(input("Quantidade de Maças: "))

if account_apple >= 12:
    print("O total de maças é: ",float(0.25 * account_apple))
else: 
    print("Seu total de maças é: ",float(0.30 * account_apple))