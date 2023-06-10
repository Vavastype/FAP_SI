'''

25) Escreva um programa para o jogo "Pedra, papel e tesoura". Neste jogo, dois jogadores escolhem uma das três opções: pedra, papel ou tesoura. Cada jogada é comparada e o vencedor é determinado de acordo com as seguintes regras:

Pedra ganha de tesoura
Tesoura ganha de papel
Papel ganha de pedra
Se ambos escolherem a mesma opção, é empate.

'''

player_first = int(input("Digite um valor de 0° Papel, 1° Pedra, 2° Tesoura - Jogador 1°"))
player_second = int(input("Digite um valor de 0° Papel, 1° Pedra, 2° Tesoura - Jogador 2°"))

element = ["papel", "pedra", "tesoura"]

if element[player_first] == "papel" and element[player_second] == "pedra":
    print("Parabéns jogador 1: ",element[player_first],"Venceu!!! :)")
elif element[player_first] == "pedra" and element[player_second] == "tesoura":
    print("Parabéns jogador 1: ",element[player_first],"Venceu!!! :)")
elif element[player_first] == "tesoura" and element[player_second] == "papel":
    print("Parabéns jogador 1: ",element[player_first],"Venceu!!! :)")
elif element[player_second] == "papel" and element[player_first] == "pedra":
    print("Parabéns jogador 2: ",element[player_second],"Venceu!!! :)")
elif element[player_second] == "pedra" and element[player_first] == "tesoura":
    print("Parabéns jogador 2: ",element[player_second],"Venceu!!! :)")
else:
    print("Parabéns jogador 2: ",element[player_second],"Venceu!!! :)")