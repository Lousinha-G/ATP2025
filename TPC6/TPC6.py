import matplotlib.pyplot as plt

def medias(tabMeteo):
        res = []
        for x in tabMeteo:
            mediadia = (x[0], (x[1]+x[2])/2)
            res.append(mediadia)
        return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    res=""
    for data, tempmin, tempmax, precipitacao in t:
        res = res + str(data) + ";" + str(tempmin) + ";" + str(tempmax) + ";" + str(precipitacao)
        res = res + "\n"
    file.write(res)
    file.close
    return

def carregaTabMeteo(fnome):
    while True:
        try:
            tabmeteo=[]
            file = open(fnome, "r")
            for line in file:
                lista=line.strip().split(";")
                if lista == ['']:
                    continue
                data_str = lista[0].strip("()")
                ano, mes, dia = data_str.split(",")
                data = (float(ano), float(mes), float(dia))
                tempmin = float(lista[1])
                tempmax = float(lista[2])
                precip = float(lista[3])
                tabmeteo.append([data, tempmin, tempmax, precip])
            file.close()
            print(tabmeteo)
            return(tabmeteo)
        except FileNotFoundError:
            print("""Ficheiro não encontrado. Tenta novamente, ou digite "0" para voltar ao menu: \n""")
            nome = input("Digite outro ficheiro: ") + ".txt"
        if nome == "0.txt":
            return []
        else: 
            fnome = nome+".txt"
            
def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for x in tabMeteo:
        if x[1] < minima:
            minima = x[1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for x in tabMeteo:
        amplitudedia = (x[0], (x[2]-x[1]))
        res.append(amplitudedia)
    return res

def maxChuva(tabMeteo):
    pmax = tabMeteo[0][3]
    data = tabMeteo[0][0]
    for x in tabMeteo:
        if x[3]>pmax:
            pmax=x[3]
            data=x[0]
    return (data, pmax)

def diasChuvosos(tabMeteo, p):
    res = []
    for xi in tabMeteo:
        if xi[3] > p:
            a = (xi[0], xi[3])
            res.append(a)
    return res

def graftemperaturas(t):
    x = [f"{data[0]}/{data[1]}/{data[2]}" for data, tmin, tmax, prec in t]
    y_min = [tmin for data, tmin, tmax, prec in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    plt.plot(x,y_min, label="Temperatura Mínima", color="red")
    plt.plot(x,y_max, label="Temperatura Máxima", color="blue")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.xlabel("Data")
    plt.ylabel("Temperatura (ºC)")
    plt.show()

def grafpluviosidade(t):
    x = [f"{data[0]}/{data[1]}/{data[2]}" for data, tmin, tmax, prec in t]
    plt.bar(x, [prec for data, tmin, tmax, prec in t], color="c", label="Pluviosidade (mm)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.xlabel("Data")
    plt.ylabel("Precipitação (mm)")
    plt.show()
    return

menu = -1
while menu !=0:
    print("1 - Carregar tabela meteorológica")
    print("2 - Guardar tabela meteorológica")
    print("3 - Calcular a temperatura média de cada dia")
    print("4 - Temperatura mínima")
    print("5 - Amplitude térmica diária")
    print("6 - Dia de maior precipitação")
    print("7 - Dias com precipitação superior a um valor")
    print("8 - Gráfico da tabela meteorológica")
    print("0 - Sair")
    menu = int(input("Escolha uma opção: "))

    if menu == 1:
        nome=input("Qual é o nome do ficheiro que pretende carregar? ")
        t = carregaTabMeteo(nome + ".txt")
        print("Tabela carregada com sucesso.")
    
    elif menu == 2:
        nome=input("Qual é o nome do ficheiro onde pretende guardar a tabela? ") + ".txt"
        guardaTabMeteo(t, nome)

    elif menu == 3:
        print(medias(t))
    
    elif menu == 4:
        print(minMin(t))
    
    elif menu == 5:
        print(amplTerm(t))

    elif menu == 6:
        print(maxChuva(t))

    elif menu == 7:
        p = float(input("Qual é o valor de precipitação? "))
        print(diasChuvosos(t, p))
    
    elif menu == 8:
        print("""1 - Gráfico de temperaturas. \n2 - Gráfico de pluviosidade. """)
        opcao = int(input("Que opção de gráfico pretende? "))
        if opcao == 1:
            graftemperaturas(t)
        elif opcao == 2:
            grafpluviosidade(t)
        else: 
            print("Opção inválida.")
