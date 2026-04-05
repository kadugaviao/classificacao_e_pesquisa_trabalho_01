from random import randint
from time import perf_counter


def random_list(minimo, maximo, tamanho):
    random_numbers = [randint(minimo, maximo) for _ in range(tamanho)]
    return random_numbers

def medir_tempo(func, arr):
    inicio = perf_counter()

    resultado = func(arr.copy())

    fim = perf_counter()

    print(f"{func.__name__}: {fim - inicio:.8f} segundos")

    return resultado

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Intervalo inicial

    while gap > 0:
        # Realiza um Insertion Sort para cada gap.
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Compara elementos afastados pelo gap.
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        # Reduz o gap pela metade.
        gap //= 2

    return arr


def shell_sort_knuth(arr):
    n = len(arr)
    h = 1

    # 1, 4, 13, 40, 121...
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            temp = arr[i]
            j = i

            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h

            arr[j] = temp

        h //= 3

    return arr


def shell_sort_otimizado(arr):
    return shell_sort_knuth(arr)


if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]
    inv_arr = list(range(1000, 0, -1))

    print("Shell sort (com lista aleatoria):")
    for i in range(10):
        medir_tempo(shell_sort, r_arr)
        medir_tempo(shell_sort_knuth, r_arr)
        print("----------")

    print("Shell sort com lista ordenada.")
    for i in range(10):
        medir_tempo(shell_sort, ord_arr)
        medir_tempo(shell_sort_knuth, ord_arr)
        print("----------")

    print("Shell sort com lista invertida.")
    for i in range(10):
        medir_tempo(shell_sort, inv_arr)
        medir_tempo(shell_sort_knuth, inv_arr)
        print("----------")
