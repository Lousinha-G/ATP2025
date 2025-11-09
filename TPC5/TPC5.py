def criarTurma():
    turma = []
    print("Turma criada com sucesso.")
    return turma

def inserirAluno(turma, nome, id, notas):
    aluno = (nome, id, notas)
    turma.append(aluno)
    return turma

def listarTurma(turma):
    for aluno in turma:
        print(aluno)

def consultarAluno(turma, id):
    for aluno in turma:
        if aluno[1] == id:
            return aluno
    return None

def calcularMediaAluno(aluno):
    notas = aluno[2]
    media = sum(notas) / len(notas)
    return media

def calcularMediaTurma(turma):
    total_media = 0
    for aluno in turma: 
        total_media += calcularMediaAluno(aluno)
        valor = total_media / len(turma)
    return valor
    
def guardarficheiro(turma, fturma):
    file = open(fturma, "w")
    res=""
    for aluno in turma:
        res += (f"{aluno[0]}; {aluno[1]}; {aluno[2]}") + "\n"
    res = res.rstrip("\n")  # remove o último \n
    file.write(res)
    file.close()

def abrirficheiro(fturma):
    fturma1 = fturma + ".txt"
    turma = []
    file = open(fturma1, "r")
    for line in file:
        line = line.strip()
        lista = line.split("; ")
        turma.append(lista)
    print("O ficheiro foi carregado com sucesso!")
    listarTurma(turma)

menu = (-1)
while menu != 0:
    print("""Que ação deseja realizar:
          1. Criar uma turma;
          2. Inserir um aluno na turma;
          3. Listar a turma;
          4. Consultar um aluno por id;
          5. Calcular a média de um aluno;
          6. Calcular a média da turma;
          8. Guardar uma turma em ficheiro;
          9. Carregar uma turma dum ficheiro;
          0. Fechar a aplicação;""")
    menu = int(input("Introduza a opção desejada: ")) 

    if menu == 1:
        turma = criarTurma()
    
    if menu == 2:
        nome = str(input("Qual é o nome do aluno? "))
        id = int(input("Qual é o id do aluno? "))
        notaTPC = int(input("Que nota é que o aluno teve no trabalho de casa? "))
        notaProj = int(input("Que nota é que o aluno teve no projeto? "))
        notaTeste = int(input("Que nota é que o aluno teve no teste? "))
        notas = [notaTPC, notaProj, notaTeste]
        inserirAluno(turma, nome, id, notas)

    if menu == 3:
        listarTurma(turma)

    if menu == 4:
        id = int(input("Qual é o id do aluno que quer consultar? "))
        aluno = consultarAluno(turma, id)
        if aluno:
            print(aluno)
        else:
            print("Aluno não encontrado.")

    if menu == 5:
        id = int(input("Qual é o id do aluno cuja média quer calcular? "))
        aluno = consultarAluno(turma, id)
        if aluno:
            media = calcularMediaAluno(aluno)
            print(f"A média do aluno é: {media}")
        else:
            print("Aluno não encontrado.")

    if menu == 6:
        media_turma = calcularMediaTurma(turma)
        print(f"A média da turma é: {media_turma}")

    if menu == 8:
        fturma = input("Qual vai ser o nome do ficheiro que deseja criar? ") + ".txt"
        guardarficheiro(turma, fturma)
        print("O ficheiro foi guardado com sucesso!")
    
    if menu == 9:
        fturma = (input("Qual é o nome do ficheiro que deseja abrir? "))
        abrirficheiro(fturma)