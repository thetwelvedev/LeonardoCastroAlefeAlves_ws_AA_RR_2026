import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calc_ops_faz_algo(n):
    if n < 3: return 0
    total = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n + 1):
            total += j
    return total

def calc_ops_faz_algo_melhor(n):
    if n < 3: return 0
    total = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n + 1):
            total += 1
    return total

def calc_ops_n3_real(n):
    if n < 3: return 0
    total = 0
    total = n ** 3
    return total

def calc_ops_n2_real(n):
    if n < 3: return 0
    total = 0
    total = n ** 2
    return total


n_values = np.arange(3, 11)
ops_algo = [calc_ops_faz_algo(n) for n in n_values]
ops_melhor = [calc_ops_faz_algo_melhor(n) for n in n_values]
ops_n3 = [calc_ops_n3_real(n) for n in n_values]
ops_n2 = [calc_ops_n2_real(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, ops_algo, label='FazAlgo (O(n³))', color='blue', linewidth=2)
plt.plot(n_values, ops_melhor, label='FazAlgo Melhorado (O(n²))', color='red', linewidth=2)
plt.plot(n_values, ops_n3, label='(O(n³))', linestyle="--", linewidth=2)
plt.plot(n_values, ops_n2, label='(O(n²))', linestyle="--", linewidth=2)

plt.title('Comparação de Operações: FazAlgo vs FazAlgo Melhorado')#FazAlgo Melhorado
plt.xlabel('Entrada (n)')
plt.ylabel('Quantidade de Operações (iterações do loop interno)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig('comparacao_algoritmos_operacoes.png', dpi=300, bbox_inches='tight')

# Save data to CSV for reference
#df = pd.DataFrame({
#    'n': n_values,
#    'ops_faz_algo': ops_algo,
#    'ops_faz_algo_melhor': ops_melhor
#})
#df.to_csv('resultados_operacoes.csv', index=False)