import time
from concurrent.futures import ThreadPoolExecutor

# Função para somar uma parte do arquivo
def somar_parte(linhas):
    soma = 0
    for linha in linhas:
        try:
            soma += int(linha.strip())
        except:
            pass
    return soma


# Função principal para somar usando N threads
def soma_paralela(arquivo, n_threads):

    # Lê todas as linhas (com encoding corrigido)
    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        linhas = f.readlines()

    # Divide o arquivo em partes
    tamanho = len(linhas) // n_threads
    partes = []

    for i in range(n_threads):
        inicio = i * tamanho
        fim = None if i == n_threads - 1 else (i + 1) * tamanho
        partes.append(linhas[inicio:fim])

    # Executa as threads
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        resultados = executor.map(somar_parte, partes)

    return sum(resultados)


# Arquivo a ser analisado
arquivo = "numero1.txt"

# Lista de threads para testar
threads_list = [1, 2, 4, 6, 12]

tempos = {}

# Execução
for n_threads in threads_list:

    inicio = time.time()

    soma = soma_paralela(arquivo, n_threads)

    fim = time.time()
    tempo_exec = fim - inicio

    tempos[n_threads] = tempo_exec

    print(f"Threads: {n_threads}")
    print(f"Soma total: {soma}")
    print(f"Tempo de execução (s): {tempo_exec:.6f}")
    print("-" * 30)


# Cálculo de Speedup e Eficiência
tempo_1 = tempos[1]

print("\nTabela final:")
print("Threads | Tempo(s) | Speedup | Eficiência")

for n_threads in threads_list:
    tempo = tempos[n_threads]
    speedup = tempo_1 / tempo
    eficiencia = speedup / n_threads

    print(f"{n_threads:7} | {tempo:.6f} | {speedup:.2f} | {eficiencia:.2f}")