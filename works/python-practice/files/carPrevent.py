'''
21) Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h

'''

aceleration = int(input("Qual é a velocidade de seu veiculo: "))

if aceleration > 80:
    print("Você foi mutado com um valor de: ",5 * aceleration,"Reais.")
else:
    print("Velocidade agradavel.")