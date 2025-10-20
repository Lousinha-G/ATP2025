# RESUMO DO TPC3
## Data: 30/09/2025
## Autor: Pedro Lousinha
## Resumo:
Este trabalho teve o objetivo de trabalhar com listas de ints. Para a criação das listas, fiz os programas 1, e 2, que criavam uma lista aleatória de N elementos entre 1 e 100, ou uma lista de N elementos inseridos pelo utilizador, respetivamente.

Criadas as listas, foram criados os programas 3, 4, 5, 6, 7, 8 e 9, que, respetivamente, realizavam as seguintes tarefas:

- somaList(list), devolve a soma da lista
- meanList(list), devolve a média da lista
- maxList(list) ou minList(list), devolvem, respetivamente o maior e menor int da lista
- isMintoMax(list) ou isMaxtoMin(list), indicam se a lista estiver, respetivamente, por ordem crescente ou decrescente
- findElement(list, elem), devolve o index da primeira aparição do elem na lista, se não existir na lista devolve -1

Criei um menu que dá um print de todas as opões possiveis do programa, ou seja, uma interface de texto.
Utilizando o código "while menu != 0", 'menu' recebe o int(input) do usuário com o número da opção que quer realizar, 1 a 9, e se menu = 0, o programa sai do loop e dá print a uma mensagem de terminação.