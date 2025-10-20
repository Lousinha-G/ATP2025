import random
fosforos = 21
quem_começa = 0
while quem_começa not in [1, 2]:
    quem_começa = int(input(f'Quem começa a jogar? Escreva 1, para começar o jogador, escreva 2, para começar o computador:'))
jogada_valida = False
if quem_começa == 1:
    vez_do_humano = True
else:
    vez_do_humano = False
while fosforos > 0:
    if vez_do_humano:
        while not jogada_valida:
            jogada = int(input(f'Estão {fosforos} em jogo, quantos fósforos, de 1 a 4, vai retirar?'))
            if jogada not in range(1, 5):
                jogada_valida = False
                print("Jogada não válida!")
            else:
                jogada_valida = True
    else:
        if fosforos in [2, 7, 12, 17]:
            jogada = 1
        elif fosforos in [3, 8, 13, 18]:
            jogada = 2
        elif fosforos in [4, 9, 14, 19]:
            jogada = 3
        elif fosforos in [5, 10, 15, 20]:
            jogada = 4
        else:
            jogada = random.randint(1, 4)
        print(f'Retirei {jogada} fósforos!')
    fosforos = fosforos - jogada
    jogada_valida = False
    if fosforos <= 0:
        if vez_do_humano:
            print("Terminou o jogo. Vitória do Computador!")
        else:
            print("Terminou o jogo. Vitória do Jogador!")
    else:
        print(f'Estão {fosforos} fósforos em jogo.')
    vez_do_humano = not vez_do_humano