import numpy as np
import matplotlib.pyplot as plt

# eixo discreto
n = np.arange(-10, 11)

# =========================
# 1. IMPULSO UNITÁRIO
# =========================
delta = np.where(n == 0, 1, 0)

plt.figure()
plt.stem(n, delta)
plt.title("Impulso Unitário δ[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("resultados/impulso.png")
plt.close()

# =========================
# 2. DEGRAU UNITÁRIO
# =========================
u = np.where(n >= 0, 1, 0)

plt.figure()
plt.stem(n, u)
plt.title("Degrau Unitário u[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("resultados/degrau.png")
plt.close()

# =========================
# 3. DESLOCAMENTO (ATRASO)
# =========================
x = np.where(n >= 0, 1, 0)
x_atrasado = np.where(n - 3 >= 0, 1, 0)

plt.figure()
plt.stem(n, x, label="Original")
plt.stem(n, x_atrasado, linefmt='r-', markerfmt='ro', label="Atrasado (3)")
plt.title("Deslocamento no Tempo")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.savefig("resultados/deslocamento.png")
plt.close()

# =========================
# 4. SISTEMA COM MEMÓRIA
# y[n] = x[n] + x[n-1]
# =========================
x_shift = np.roll(x, 1)
y = x + x_shift

plt.figure()
plt.stem(n, y)
plt.title("Sistema: y[n] = x[n] + x[n-1]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("resultados/sistema.png")
plt.close()

# =========================
# 5. SINAL EXPONENCIAL
# =========================
a = 0.8
x_exp = a**n

plt.figure()
plt.stem(n, x_exp)
plt.title("Sinal Exponencial Discreto (a = 0.8)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("resultados/exponencial.png")
plt.close()

print("✅ Todos os gráficos foram gerados com sucesso!")
