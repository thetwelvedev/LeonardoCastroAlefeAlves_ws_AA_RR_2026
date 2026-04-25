import matplotlib.pyplot as plt
import numpy as np

# Lendo o arquivo
n = []
tempo_ns = []

with open("resultados.txt", "r") as f:
    next(f)  # pula o cabeçalho
    for line in f:
        parts = line.strip().split(",")
        n.append(int(parts[0]))
        tempo_ns.append(float(parts[1]))

n = np.array(n)
tempo_ns = np.array(tempo_ns)

# Conversão para segundos
tempo_s = tempo_ns / 1e9

# =========================
# GRÁFICO PRINCIPAL (SEGUNDOS)
# =========================
plt.figure(figsize=(10,6))
plt.plot(n, tempo_s, marker='o', label="Tempo real (s)")

plt.title("Tempo de execução vs Entrada")
plt.xlabel("Entrada (n)")
plt.ylabel("Tempo (segundos)")
plt.grid(True)
plt.legend()

plt.savefig("grafico_tempo_segundos.png", dpi=300, bbox_inches="tight")

plt.show()

# =========================
# ANÁLISE ASSINTÓTICA
# =========================

n_norm = n / n.max()
n_log_n = (n * np.log2(n)) / (n * np.log2(n)).max()
n_quad = (n**2) / (n**2).max()
tempo_norm = tempo_s / tempo_s.max()

plt.figure(figsize=(10,6))

plt.plot(n, tempo_norm, label="Real (normalizado)", marker='o')
plt.plot(n, n_norm, label="O(n)", linestyle="--")
plt.plot(n, n_log_n, label="O(n log n)", linestyle="--")
plt.plot(n, n_quad, label="O(n²)", linestyle="--")

plt.title("Comparação de comportamento assintótico")
plt.xlabel("Entrada (n)")
plt.ylabel("Escala normalizada")
plt.grid(True)
plt.legend()

plt.show()

# =========================
# ESTIMATIVA DE COMPLEXIDADE
# =========================

log_n = np.log(n)
log_t = np.log(tempo_s)

coef = np.polyfit(log_n, log_t, 1)
expoente = coef[0]

print(f"Estimativa de crescimento: T(n) ≈ n^{expoente:.2f}")
