import time
from concurrent.futures import ThreadPoolExecutor

# Função que soma uma lista de números
def somar_parte(lista):
    return sum(lista)

# Função para ler o arquivo em blocos e converter para números
def ler_em_blocos(arquivo, bloco_size=1000000):
    bloco = []

    # leitura corrigida (resolve UnicodeDecodeError)
    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            try:
                bloco.append(int(linha.strip()))
            except:
                continue

            if len(bloco) == bloco_size:
                yield bloco
                bloco = []

        if bloco:
            yield bloco

# Função principal para somar com threads
def soma_paralela(arquivo, n_threads):

    blocos = list(ler_em_blocos(arquivo))

    # Divide blocos entre threads
    partes = [[] for _ in range(n_threads)]

    for i, bloco in enumerate(blocos):
        partes[i % n_threads].extend(bloco)

    # Soma em paralelo
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        resultados = executor.map(somar_parte, partes)

    return sum(resultados)


# Arquivo a ser analisado
arquivo = "numero2.txt"

# Quantidade de threads
threads_list = [1, 2, 4, 8, 12]

# Guardar tempos
tempos = {}

# Rodar o experimento
for n_threads in threads_list:

    inicio = time.time()

    soma = soma_paralela(arquivo, n_threads)

    fim = time.time()

    tempos[n_threads] = fim - inicio

    print(f"Threads: {n_threads}")
    print(f"Soma total: {soma}")
    print(f"Tempo de execução (s): {tempos[n_threads]:.6f}")
    print("-" * 30)

# Calcular Speedup e Eficiência
tempo_1 = tempos[1]

print("\nTabela final:")
print("Threads | Tempo(s) | Speedup | Eficiência")

for n_threads in threads_list:

    tempo = tempos[n_threads]

    speedup = tempo_1 / tempo
    eficiencia = speedup / n_threads

    print(f"{n_threads:7} | {tempo:.6f} | {speedup:.2f} | {eficiencia:.2f}")