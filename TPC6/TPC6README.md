# RESUMO DO TPC6
## Data: 21/10/2025
## Autor: Pedro Lousinha
## Resumo:
Este trabalho teve como objetivo criar um programa de gestão de um ficheiro de metereologia.
O programa contem as seguintes estruturas de dados:

- TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
    - Data = (Int,Int,Int)
    - TempMin = Float
    - TempMax = Float
    - Precipitacao = Float

A aplicação apresenta as seguintes funções:
- carregar ficheiro de tabela metereológica;
- guardar ficheiro de tabela metereológica;
- calcular a temperatura média de cada dia;
- determinar a temperatura mínima;
- calcular a amplitude térmica diária;
- determinar o dia de maior precipitação;
- listar os dias com precipitação superior a um valor dado;
- apresentar um gráfico da tabela metereológica com opção de temperaturas ou pluviometria.

O programa foi implementado utilizando a biblioteca Matplotlib para a criação dos gráficos. A interface do utilizador é baseada em texto, permitindo uma interação simples e direta com o utilizador.