import matplotlib.pyplot as plt
import numpy as np

# =========================
# FUNÇÃO PARA LER ARQUIVO
# =========================
def ler_dados(arquivo):
    n = []
    tempo_ns = []

    with open(arquivo, "r") as f:
        next(f)  # pula cabeçalho

        for line in f:
            parts = line.strip().split(",")
            n.append(int(parts[0]))
            tempo_ns.append(float(parts[1]))

    return np.array(n), np.array(tempo_ns)


# =========================
# LENDO OS DOIS ALGORITMOS
# =========================

# FazAlgo
n1, tempo1_ns = ler_dados("resultados.txt")

# FazMelhor
n2, tempo2_ns = ler_dados("resultadosM.txt")


# converter para segundos
tempo1_s = tempo1_ns / 1e9
tempo2_s = tempo2_ns / 1e9


# =========================
# GRÁFICO DE TEMPO
# =========================
plt.figure(figsize=(10,6))

plt.plot(n1, tempo1_s,
         marker='o',
         label="FazAlgo")

plt.plot(n2, tempo2_s,
         marker='s',
         label="FazMelhor")

plt.title("Comparação de Tempo de Execução")
plt.xlabel("Entrada (n)")
plt.ylabel("Tempo (segundos)")
plt.grid(True)
plt.legend()

plt.savefig("comparacao_tempos.png",
            dpi=300,
            bbox_inches="tight")

plt.show()



# =========================
# ANÁLISE ASSINTÓTICA
# =========================

# normalizações FazAlgo
tempo1_norm = tempo1_s / tempo1_s.max()

# normalizações FazMelhor
tempo2_norm = tempo2_s / tempo2_s.max()

# curvas teóricas
n_norm = n1 / n1.max()
n_log_n = (n1*np.log2(n1)) / (n1*np.log2(n1)).max()
n_quad = (n1**2)/(n1**2).max()


plt.figure(figsize=(10,6))

# reais
plt.plot(n1, tempo1_norm,
         marker='o',
         label="FazAlgo")

plt.plot(n2, tempo2_norm,
         marker='s',
         label="FazMelhor")

# assintóticas
plt.plot(n1, n_norm,
         '--',
         label="O(n)")

plt.plot(n1, n_log_n,
         '--',
         label="O(n log n)")

plt.plot(n1, n_quad,
         '--',
         label="O(n²)")

plt.title("Comparação de comportamento assintótico")
plt.xlabel("Entrada (n)")
plt.ylabel("Escala normalizada")

plt.grid(True)
plt.legend()

plt.savefig("analise_assintotica.png",
            dpi=300,
            bbox_inches="tight")

plt.show()



# =========================
# ESTIMATIVA DE COMPLEXIDADE
# =========================

# FazAlgo
coef1 = np.polyfit(np.log(n1), np.log(tempo1_s), 1)
exp1 = coef1[0]

# FazMelhor
coef2 = np.polyfit(np.log(n2), np.log(tempo2_s), 1)
exp2 = coef2[0]

print(f"FazAlgo   -> T(n) ≈ n^{exp1:.2f}")
print(f"FazMelhor -> T(n) ≈ n^{exp2:.2f}")
