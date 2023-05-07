'''
14) Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.


'''

user_playerFirst = input("Seu primeiro time preferido: ")
rank_playerFirst = int(input("Quandidade de Marcação: "))

user_playeSecond = input("Seu segundo time preferido: ")
rank_playerSecond = int(input("Quandidade de Marcação: "))

if rank_playerFirst > rank_playerSecond:
    print(user_playerFirst,"Foi O time com mais marcações do que o adversario:",rank_playerFirst)
elif rank_playerSecond > rank_playerFirst:
    print(user_playeSecond,"Foi O time com mais marcações do que o adversario:",rank_playerSecond)
else:
    print("O placar ficou em empate por:",rank_playerFirst,"no adversario:",user_playerFirst," | ", rank_playerSecond,"no adversario",user_playeSecond)