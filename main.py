import function
import time

inicio = time.time()
lista = []

while True:
    print('1. Insection Sort')
    print('2. Bubble Sort')
    print('3. Selection Sort')
    print('4. Pigeonhole Sort')
    ord = int(input('Qual tipo de ordenação deseja: '))
    if ord >= 5 or ord < 1:
        print('Opção inválida!')
        break

    qnt = int(input('Quantidade de valores para ordenar: '))
    for x in range(qnt):
        val = int(input('Digite um valor: '))
        lista.append(val)
    
    if ord == 1:
        print('ordenação por Insection Sort: ', function.insertion_sort(lista))
    elif ord == 2:
        print('Ordenação por Bubble Sort: ', function.bubble_sort(lista))
    elif ord == 3:
        print('Ordenação por Selection Sort: ', function.selection_sort(lista))
    elif ord == 4: 
        print('Ordenação por Pigeonhole Sort: ', function.pigeohole_sort(lista))

    break

fim = time.time()
dif = fim - inicio
print(f'Tempo de execução: {dif} s')