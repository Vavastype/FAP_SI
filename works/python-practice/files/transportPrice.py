'''
22) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

'''

distance = int(input("Digite o valor de distancia deseja percorrer: "))

if distance <= 200:
    print("Esse é o total para viagem de 200Km: $",0.50 * distance,"Reais")
else:
    print("Esse é o total para viagem acima de 200Km: $",0.45 * distance,"Reais")