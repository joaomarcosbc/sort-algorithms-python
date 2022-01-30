def insertion_sort(lista):

    i = 1
    while i < len(lista):
        temp = lista[i]
        trocou = False
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j+1] = lista[j]
            trocou = True
            j -= 1
        if trocou:
            lista[j+1] = temp
        i += 1

    return lista


def bubble_sort(lista):

    for final in range(len(lista), 0, -1):
        troca = False
        for current in range(0, final - 1):
            if lista[current] > lista[current + 1]:
                lista[current + 1], lista[current] = lista[current], lista[current + 1]
                troca = True
        if not troca:
            break

    return lista


def selection_sort(lista):
    for c in range(0, len(lista)):
        min_c = c

        for right in range(c + 1, len(lista)):
            if lista[right] < lista[min_c]:
                min_c = right

        lista[c], lista[min_c] = lista[min_c], lista[c]

    return lista


def pigeohole_sort(lista):
    mini = min(lista)
    maxi = max(lista)
    tam = maxi - mini + 1

    holes = [0] * tam
    for i in lista:
        assert type(i) is int, "São inteiros"
        holes[i - mini] += 1

    a = 0
    for c in range(tam):
        while holes[c]>0:
            holes[c] -=1
            lista[a] = c + mini
            a += 1

    return lista