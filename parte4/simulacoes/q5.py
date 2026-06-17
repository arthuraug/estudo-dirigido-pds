import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter

# ==========================
# Parâmetros do filtro
# ==========================
fs = 1000          # Frequência de amostragem (Hz)
fc = 100           # Frequência de corte (Hz)
ordem = 4

# ==========================
# Projeto do filtro IIR Butterworth
# ==========================
b, a = butter(ordem, fc / (fs / 2), btype='low')

# ==========================
# Cálculo dos polos e zeros
# ==========================
zeros = np.roots(b)
polos = np.roots(a)

# ==========================
# Círculo unitário
# ==========================
theta = np.linspace(0, 2*np.pi, 500)

plt.figure(figsize=(6,6))

plt.plot(np.cos(theta), np.sin(theta),
         linestyle='--', label='Círculo unitário')

# Zeros
plt.scatter(np.real(zeros),
            np.imag(zeros),
            marker='o',
            s=80,
            label='Zeros')

# Polos
plt.scatter(np.real(polos),
            np.imag(polos),
            marker='x',
            s=80,
            label='Polos')

plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")

plt.title("Mapa de Polos e Zeros")

plt.axis('equal')
plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q5_polos_zeros.png",
            dpi=300)

plt.close()

print("Questão 5 executada com sucesso.")