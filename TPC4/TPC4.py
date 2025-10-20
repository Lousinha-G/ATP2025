def listar(cinema):
    for sala in cinema:
        print(sala[2])

def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme:
            return lugar not in sala[1]

def vendebilhete(cinema, filme, lugar):
    for i in range (len(cinema)):
        if cinema[i][2] == filme:
            cinema[i][1].append(lugar)
    return cinema

def listardisponibilidades(cinema):
    for i in range(len(cinema)):
        print(f"O filme em exibição na sala {i+1} é {cinema[i][2]} e esta tem {cinema[i][0] - len(cinema[i][1])} lugares disponíveis.")

def inserirSala(cinema, sala):
    if sala in cinema:
        return "Esta sala já existe no cinema."
    else: 
        cinema.append(sala)
        return cinema

sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema = [sala1, sala2]

menu = (-1)
lista = []
while menu != 0:
    print("""Que ação deseja realizar:
          1. Listar todos os filmes em exibição neste momento;
          2. Saber se um lugar está disponível;
          3. Vender um bilhete de cinema;
          4. Listar as disponibilidades de todas as salas;
          5. Inserir uma nova sala no cinema;
          0. Fechar a aplicação;""")
    menu = int(input("Introduza a opção desejada: "))
    
    if menu ==  1:
        listar(cinema)

    if menu ==  2:
        filme = input("Qual o filme que deseja verificar? ")
        lugar = input("Qual o lugar que deseja verificar? ")
        if disponivel(cinema, filme, lugar):
            print("O lugar está disponível.")
        else:
            print("O lugar não está disponível.")

    if menu ==  3:
        filme = input("Qual o filme que deseja ver? ")
        lugar = input("Qual o lugar que deseja ver? ")
        cinema = vendebilhete(cinema, filme, lugar)
        print("Bilhete vendido com sucesso.")
        
    if menu ==  4:
        listardisponibilidades(cinema)

    if menu ==  5:
        lugares = int(input("Quantos lugares tem a nova sala? "))
        filme = input("Qual o filme que deseja exibir na nova sala? ")
        sala = (lugares, [], filme)
        cinema = inserirSala(cinema, sala)

    if menu ==  0: 
        print("A aplicação foi fechada com sucesso.")