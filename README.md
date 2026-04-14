# FazAlgo

## Seminário de Análise de Algoritmos

---

**Integrantes:** [Leonardo Castro](https://github.com/thetwelvedev) e [Álefe Alves](https://github.com/AlefeAlvesC)

**Descrição:**
Este trabalho tem como objetivo analisar a complexidade computacional de um algoritmo denominado FazAlgo, considerando sua função de custo, comportamento assintótico e desempenho prático por meio de experimentação.
Além disso, será proposta uma versão mais eficiente do algoritmo, comparando os resultados obtidos em termos de tempo de execução.

---

## 📑 Índice

* [Objetivos](#objetivos)
* [Algoritmo Analisado](#algoritmo-analisado)
* [Análise de Complexidade](#análise-de-complexidade)
* [Experimentação](#experimentação)
* [Resultados](#resultados)
* [Conclusão](#conclusão)
* [Referências](#referências)

---

## Objetivos

* Determinar a função de custo e complexidade do algoritmo
* Implementar o algoritmo em linguagem C
* Experimentar a execução do algoritmo com diferentes entradas e coletar tempos de execução
* Construir gráfico de linha relacionando entrada × tempo de execução
* Analisar a tendência assintótica
* Propor um algoritmo mais eficiente

---

## Algoritmo Analisado

```c
void FazAlgo (int n) {
    int i, j, k;
    for (i = 1; i < n - 1; i++) {
        for (j = 2; j <= n; j++) {
            for (k = 1; k <= j; k++) {
                // Algum comando de custo O(1)
            }
        }
    }
}
```

---

## Análise de Complexidade

A análise será baseada na contagem de operações fundamentais dentro dos laços aninhados, levando à determinação da função de custo e sua notação assintótica.

---

## Experimentação

Serão realizados testes variando o valor de `n`, registrando o tempo de execução para cada entrada.

Ferramentas sugeridas:

* Linguagem C
* Função `clock()` ou `gettimeofday`
* Exportação de dados para CSV

---

## Resultados

Os resultados serão apresentados em forma de gráfico (tempo × entrada), permitindo observar o crescimento da função e validar a complexidade teórica.

---

## Conclusão

Discussão sobre:

* Complexidade encontrada
* Diferença entre teoria e prática
* Comparação com algoritmo otimizado

---

## Referências

* CORMEN, Thomas H. et al. *Algoritmos: teoria e prática*. 3. ed. Rio de Janeiro: Elsevier, 2012.
