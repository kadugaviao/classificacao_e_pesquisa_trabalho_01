import time
import random


def random_list(min, max, tamanho):
    random_numbers = [random.randint(min, max) for _ in range(tamanho)]
    return random_numbers

def medir_tempo(func, arr):
    inicio = time.perf_counter()
    
    resultado = func(arr.copy())

    fim = time.perf_counter()

    print(f"{func.__name__}: {fim - inicio:.8f} segundos")

    return resultado

def bubble_sort1(arr):
    n = len(arr)

    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def bubble_sort2(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    for i in range(0, n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                houve_troca = True

        if not houve_troca:
            break

    return arr

if __name__ == "__main__":
    r_arr = random_list(0, 1001, 1000)
    ord_arr = [i for i in range(0, 1000)]
    inv_arr = list(range(1000, 0, -1))

    print("Bubble sort (com lista aleatoria):")
    for i in range(10):
        medir_tempo(bubble_sort1, r_arr)
        medir_tempo(bubble_sort2, r_arr)
        print("----------")

    print("Bubble sort com lista ordenada.")
    for i in range(10):
        medir_tempo(bubble_sort1, ord_arr)
        medir_tempo(bubble_sort2, ord_arr)
        print("----------")

    print("Bubble sort com lista invertida.")
    for i in range(10):
        medir_tempo(bubble_sort1, inv_arr)
        medir_tempo(bubble_sort2, inv_arr)
        print("----------")

