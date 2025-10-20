import random
menu = (-1)
lista = []
while menu != 0:
    print("""Que ação deseja realizar:
          1. Criar uma lista aleatória;
          2. Criar uma lista com números inseridos pelo utilizador;
          3. Calcular a soma dos elementos da lista criada;
          4. Calcular a média dos elementos da lista criada;
          5. Apresentar o maior elemento da lista criada;
          6. Apresentar o menor elemento da lista criada;
          7. Indicar se a lista está ordenada por ordem crescente;
          8. Indicar se a lista está ordenada por ordem decescente;
          9. Procurar um elemento na lista, e indicar a sua posição, ou responder "-1" caso este não pertença à lista;
          0. Fechar a aplicação;""")
    
    menu = int(input("Que ação deseja realizar?"))

    if menu ==  1:
        lista = []
        numeroelems = int(input("Introduza um número N, para a quantidade de elementos da lista"))
        lista += [random.randrange(1, 101) for x in range (numeroelems)]
        print(lista)

    if menu == 2:
        lista = []
        numerooo = int(input("Introduza um número N, para a quantidade de elementos da lista"))
        for i in range(numerooo):
            balls = int(input(f'Adicione um número à lista {i+1}/{numerooo}'))
            lista.append(balls)
        print(lista)

    if menu == 3:
        soma = 0
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            for numero in lista:
                soma = soma + numero
            print(soma)

    if menu == 4:
        soma = 0
        if len(lista) == 0:
                print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            for numero in lista:
                soma = soma + numero
            media = soma / len(lista)
            print(media)

    if menu == 5:
        maior = 0
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            for x in lista:
                if x > maior:
                    maior = x
            print(maior)

    if menu == 6:
        menor = 101
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            for x in lista:
                if x < menor:
                    menor = x
            print(menor)

    if menu == 7:
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            res = True
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    res = False
            if res == True:
                print("A lista está ordenada por ordem crescente")
            else: 
                print("A lista não está ordernada por ordem crescente")

    if menu == 8:
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            res = True
            for i in range(len(lista) - 1):
                if lista[i] < lista[i + 1]:
                    res = False
            if res == True:
                print("A lista está ordenada por ordem decrescente")
            else: 
                print("A lista não está ordernada por ordem decrescente")

    if menu == 9:
        if len(lista) == 0:
            print("Selecione a opção 1, ou 2, para criar uma lista primeiro.")
        else: 
            tamanho = len(lista)
            i = 0
            elem = int(input("Introduza o numero que pretende procurar na lista: "))
            if elem in lista :
                while i < tamanho :
                    if lista[i] == elem :
                        print(f"A sua posição é {i + 1}.")
                        i = tamanho
                    else :
                        i = i + 1
            else :
                print("A sua posição é -1.")

print("Fim do programa.")