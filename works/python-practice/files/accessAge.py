'''
19 Condição para Votar Faça um programa que receba a idade de uma pessoa e imprima sua condição (obrigatória, optativa ou proibida), em relação ao ato de votar, conforme apresentado abaixo:

- Pessoas com idade menor que 16 anos são proibidas de votar (proibido);

- Pessoas com idade igual a 16 e menor que 18 anos não são obrigadas a votar (optativo);

- Pessoas com idade igual a 18 e menor que 65 anos são obrigadas a votar (obrigatório);

- Pessoas com idade igual ou maior a 65 anos não são obrigadas a votar (optativo).

'''
status_age = int(input("Digite sua idade: "))

if status_age < 16:
    print("Desculpa sua idade não é acessivel para Votação Eletronica.")
elif status_age >= 16 and status_age < 18:
    print("Você possui disponibilidade de votar, mas não é obrigatorio. A ainda ( ͡° ͜ʖ ͡°)")
elif status_age >= 18 and status_age < 65:
    print("Apartir dessa idade 18 até 64 anos você é obrigatorio para votação.")
else:
    print("Você titular de 64 anos, acima dessa idade não é obrigatorio sua votação.")