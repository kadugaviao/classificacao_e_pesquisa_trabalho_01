from random import randint
from time import perf_counter
from bubble_sort import bubble_sort1, bubble_sort2
from insertion_sort import insertion_sort, insertion_sort_binary
from selection_sort import cocktail_selection_sort, selection_sort
from shellsort import shell_sort, shell_sort_otimizado

def random_list(minimo, maximo, tamanho):
	return [randint(minimo, maximo) for _ in range(tamanho)]

def medir_tempo(func, arr):
	inicio = perf_counter()
	func(arr.copy())
	fim = perf_counter()
	return fim - inicio


def medir_media(func, arr, repeticoes):
	# Execucao de aquecimento para reduzir variacoes de primeira chamada.
	medir_tempo(func, arr)

	total = 0.0
	for _ in range(repeticoes):
		total += medir_tempo(func, arr)
	return total / repeticoes

def formatar_celula(tempo, tempo_contraparte):
	if tempo_contraparte == 0:
		diferenca = 0.0
	else:
		diferenca = ((tempo_contraparte - tempo) / tempo_contraparte) * 100
	return f"{tempo:.8f}s ({diferenca:+.2f}%)"


def imprimir_tabela(resultados, ordem_colunas, contraparte):
	cabecalho = ["Algoritmo"] + [titulo for titulo, _ in ordem_colunas]

	linhas = []
	for nome_algoritmo in resultados:
		linha = [nome_algoritmo]
		nome_contraparte = contraparte[nome_algoritmo]
		for _, chave_cenario in ordem_colunas:
			tempo = resultados[nome_algoritmo][chave_cenario]
			tempo_contraparte = resultados[nome_contraparte][chave_cenario]
			linha.append(formatar_celula(tempo, tempo_contraparte))
		linhas.append(linha)

	larguras = [len(texto) for texto in cabecalho]
	for linha in linhas:
		for i, texto in enumerate(linha):
			larguras[i] = max(larguras[i], len(texto))

	def montar_linha(colunas):
		return " | ".join(colunas[i].ljust(larguras[i]) for i in range(len(colunas)))

	print("Tabela de tempos (valor em segundos e % relativo a contraparte; negativo = pior)")
	print(montar_linha(cabecalho))
	print("-+-".join("-" * largura for largura in larguras))
	for linha in linhas:
		print(montar_linha(linha))


def main():
	tamanho = 1000
	repeticoes = 20

	arr_aleatoria = random_list(0, 10000, tamanho)
	arr_ordenada = [i for i in range(tamanho)]
	arr_invertida = list(range(tamanho, 0, -1))

	algoritmos = [
		("Bubble Sort", bubble_sort1),
		("Bubble Sort Otimizado", bubble_sort2),
		("Selection Sort", selection_sort),
		("Selection Cocktail", cocktail_selection_sort),
		("Insertion Sort", insertion_sort),
		("Insertion Binario", insertion_sort_binary),
		("Shell Sort", shell_sort),
		("Shell Sort Otimizado", shell_sort_otimizado),
	]

	ordem_colunas = [
		("Aleatoria", "aleatoria"),
		("Ordenada", "ordenada"),
		("Invertida", "invertida"),
	]

	contraparte = {
		"Bubble Sort": "Bubble Sort Otimizado",
		"Bubble Sort Otimizado": "Bubble Sort",
		"Selection Sort": "Selection Cocktail",
		"Selection Cocktail": "Selection Sort",
		"Insertion Sort": "Insertion Binario",
		"Insertion Binario": "Insertion Sort",
		"Shell Sort": "Shell Sort Otimizado",
		"Shell Sort Otimizado": "Shell Sort",
	}

	cenarios = {
		"aleatoria": {"array": arr_aleatoria},
		"ordenada": {"array": arr_ordenada},
		"invertida": {"array": arr_invertida},
	}

	resultados = {}

	for nome, func in algoritmos:
		resultados[nome] = {}
		for _, chave_cenario in ordem_colunas:
			tempo = medir_media(func, cenarios[chave_cenario]["array"], repeticoes)
			resultados[nome][chave_cenario] = tempo

	imprimir_tabela(resultados, ordem_colunas, contraparte)


if __name__ == "__main__":
	main()
