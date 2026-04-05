from random import randint
from time import perf_counter

def medir_tempo(func, arr):
    inicio = perf_counter()

    resultado = func(arr.copy())

    fim = perf_counter()

    tempo = fim - inicio

    print(f"{func.__name__}: {tempo:.8f}")
    return resultado

def random_list(min, max, tamanho):
    random_numbers = [randint(min, max) for _ in range(tamanho)]
    return random_numbers


def selection_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
            
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

    return arr

def cocktail_selection_sort(arr):
    n = len(arr)

    for i in range(0, n // 2):
        min_index = i
        max_index = n - i - 1
        for j in range(i + 1, n - i - 1):
            if arr[j] < arr[min_index]:
                min_index = j
            if arr[j] > arr[max_index]:
                max_index = j

        arr[n - i - 1], arr[max_index] = arr[max_index], arr[n - i - 1]

        if min_index == n - i - 1:
            min_index = max_index

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = random_list(0, 5000, 5000)

    for i in range(10):
        medir_tempo(selection_sort, arr)
        medir_tempo(cocktail_selection_sort, arr)
        print("------------")
