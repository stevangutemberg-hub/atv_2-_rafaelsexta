# atv_2-_rafaelsexta
# Relatório da NOME DA ATIVIDADE

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA
**Aluno(s):** STEVAN GUTEMBERG SILVA SERPA 
**Turma:** ANALISE E DESENVOLVIMENTO DE SISTEMAS 
**Professor:** RAFAEL
**Data:** 13/03/2026

---

# 1. Descrição do Problema

O problema proposto foi desenvolver um programa capaz de realizar a soma de uma grande quantidade de números armazenados em arquivos de texto. O objetivo foi analisar o desempenho da execução utilizando paralelismo com diferentes quantidades de threads.

O algoritmo utilizado consiste em ler os números do arquivo, dividir os dados em partes e distribuir essas partes entre várias threads. Cada thread realiza a soma de uma parte dos dados e ao final os resultados são somados para gerar a soma total.

Nos testes foram utilizados arquivos contendo até 10 milhões de números, permitindo avaliar o comportamento do algoritmo com grandes volumes de dados.

---

# 2. Ambiente Experimental

Descreva o ambiente em que os experimentos foram realizados.

## Orientações

Informar as características do hardware e software utilizados na execução dos testes.

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 | Processador do computador utilizado          |
| Número de núcleos           |   12        |
| Memória RAM                 |   8 GB        |
| Sistema Operacional         |      Windows     |
| Linguagem utilizada         |      Python     |
| Biblioteca de paralelização |      concurrent.futures     |
| Compilador / Versão         |      Python 3     |

---

# 3. Metodologia de Testes

Os testes foram realizados executando o programa com diferentes quantidades de threads para analisar o impacto do paralelismo no tempo de execução.

O tempo foi medido utilizando a função time() da biblioteca time do Python, registrando o início e o fim da execução.

Foram realizadas execuções com diferentes quantidades de threads para comparar o desempenho e posteriormente calcular o speedup e a eficiência.

Configurações testadas

1 thread (execução serial)

2 threads

4 threads

8 threads

12 threads

Durante os testes o programa foi executado no mesmo computador, mantendo as mesmas condições de execução.
---

# 4. Resultados Experimentais

Preencha a tabela com os **tempos médios de execução** obtidos.

## Orientações

* O tempo deve ser informado em **segundos**
* Utilizar a **média das execuções**

| Nº Threads/Processos | Tempo de Execução (s) |
| -------------------- | --------------------- |
| 1                    |           0.081            |
| 2                    |           0.081           |
| 4                    |           0.086          |
| 8                    |           0.084           |
| 12                   |             0.165          |

---

# 5. Cálculo de Speedup e Eficiência

Para avaliar o desempenho do paralelismo foram utilizados dois indicadores: speedup e eficiência.

O speedup representa o quanto o programa ficou mais rápido em comparação com a execução serial.

A eficiência indica o quanto do desempenho ideal foi alcançado considerando o número de threads utilizadas.

Esses valores foram calculados utilizando os tempos de execução obtidos nos experimentos.

# 6. Tabela de Resultados

Preencha a tabela abaixo utilizando os tempos medidos.

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
| ----------------- | --------- | ------- | ---------- |
| 1                 |     0.081      | 1.0     | 1.0        |
| 2                 |    0.081       |    0.99     |      0.50      |
| 4                 |       0.086    |    0.94     |     0.24       |
| 8                 |      0.084     |    0.96     |      0.12      |
| 12                |      0.165     |    0.49     |      0.04     |

---

# 7. Gráfico de Tempo de Execução

O gráfico de tempo de execução mostra a relação entre o número de threads utilizadas e o tempo necessário para executar o programa.

Esse gráfico permite visualizar se o aumento do número de threads contribui para reduzir o tempo de execução da aplicação.

file:///C:/Users/aluno/Documents/imagemgrafico/tempo.png
---

# 8. Gráfico de Speedup

O gráfico de speedup mostra o ganho de desempenho obtido com o uso do paralelismo.

Ele permite comparar o speedup obtido com o speedup ideal, que seria um crescimento linear conforme aumenta o número de threads.

file:///C:/Users/aluno/Documents/imagemgrafico/speedup.png
---

# 9. Gráfico de Eficiência

O gráfico de eficiência apresenta o aproveitamento do paralelismo conforme aumenta o número de threads.

Valores próximos de 1 indicam melhor aproveitamento dos recursos de processamento.

file:///C:/Users/aluno/Documents/imagemgrafico/efici%C3%AAncia.png
---

# 10. Análise dos Resultados

Os resultados obtidos mostram que o speedup não foi significativamente superior ao da execução serial. Em alguns casos, o tempo de execução até aumentou com o uso de mais threads.

Isso pode ocorrer devido ao overhead de gerenciamento das threads, que inclui criação, sincronização e divisão do trabalho.

Outro fator importante é que a leitura do arquivo e o acesso à memória podem se tornar gargalos, limitando o ganho obtido com a paralelização.

Observa-se também que a eficiência diminui à medida que o número de threads aumenta. Isso indica que a aplicação não escala perfeitamente com o aumento do paralelismo.

Além disso, quando o número de threads se aproxima ou ultrapassa o número de núcleos disponíveis no processador, o sistema operacional precisa alternar entre as threads, aumentando o custo de gerenciamento.
---

# 11. Conclusão

O experimento demonstrou o funcionamento do processamento paralelo utilizando threads na linguagem Python.

Embora a paralelização permita dividir o trabalho entre múltiplas threads, o ganho de desempenho depende de diversos fatores, como o tipo de tarefa executada, o acesso à memória e o overhead de criação das threads.

Nos resultados obtidos, o aumento do número de threads não trouxe um ganho significativo de desempenho, indicando que a aplicação possui limitações relacionadas ao gerenciamento de threads e ao acesso aos dados.

Mesmo assim, o experimento foi importante para compreender conceitos fundamentais de paralelismo, speedup e eficiência, além de demonstrar na prática o impacto do paralelismo no desempenho de aplicações.

---
