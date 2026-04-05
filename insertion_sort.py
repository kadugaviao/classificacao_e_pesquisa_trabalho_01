from random import randint
from time import perf_counter


def medir_tempo(func, arr):
    inicio = perf_counter()

    resultado = func(arr.copy())

    fim = perf_counter()

    tempo = fim - inicio

    print(f"{func.__name__}: {tempo:.8f} segundos")
    return resultado


def random_list(min, max, tamanho):
    random_numbers = [randint(min, max) for _ in range(tamanho)]
    return random_numbers


def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave
    return arr


def busca_binaria(arr, item, baixo, alto):
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = arr[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return baixo


def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        chave = arr[i]

        posicao = busca_binaria(arr, chave, 0, i - 1)

        j = i - 1
        while j >= posicao:
            arr[j + 1] = arr[j]
            j -= 1

        arr[posicao] = chave

    return arr


if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]
    inv_arr = list(range(1000, 0, -1))

    print("Insertion sort (com lista aleatoria):")
    for i in range(10):
        medir_tempo(insertion_sort, r_arr)
        medir_tempo(insertion_sort_binary, r_arr)
        print("----------")

    print("Insertion sort com lista ordenada.")
    for i in range(10):
        medir_tempo(insertion_sort, ord_arr)
        medir_tempo(insertion_sort_binary, ord_arr)
        print("----------")

    print("Insertion sort com lista invertida.")
    for i in range(10):
        medir_tempo(insertion_sort, inv_arr)
        medir_tempo(insertion_sort_binary, inv_arr)
        print("----------")