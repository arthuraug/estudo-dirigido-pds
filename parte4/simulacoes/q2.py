import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# ==========================
# Parâmetros
# ==========================
fs = 1000                    # Frequência de amostragem (Hz)
t = np.arange(0, 1, 1/fs)

# ==========================
# Sinal original
# ==========================
f = 50                       # Frequência do sinal (Hz)
sinal = np.sin(2 * np.pi * f * t)

# ==========================
# Ruído branco aditivo
# ==========================
np.random.seed(42)           # Garante reprodutibilidade

ruido = 0.5 * np.random.randn(len(t))

sinal_ruidoso = sinal + ruido

# ==========================
# Projeto do filtro FIR passa-baixa
# ==========================
fc = 100                     # Frequência de corte (Hz)
num_taps = 51

coef = firwin(num_taps, fc, fs=fs)

# Aplicação do filtro
sinal_filtrado = lfilter(coef, 1, sinal_ruidoso)

# ==========================
# Domínio do tempo
# ==========================
plt.figure(figsize=(10, 4))

plt.plot(t, sinal_ruidoso, label="Sinal com ruído")
plt.plot(t, sinal_filtrado, label="Sinal filtrado", linewidth=2)

plt.xlim(0, 0.1)

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Filtro FIR aplicado ao sinal com ruído")

plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q2_tempo.png", dpi=300)
plt.close()

# ==========================
# FFT
# ==========================
X = np.fft.fft(sinal_ruidoso)
Y = np.fft.fft(sinal_filtrado)

freq = np.fft.fftfreq(len(t), d=1/fs)

mask = freq >= 0

plt.figure(figsize=(10, 4))

plt.plot(freq[mask], np.abs(X)[mask], label="Com ruído")
plt.plot(freq[mask], np.abs(Y)[mask], label="Filtrado")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Espectro antes e depois da filtragem FIR")

plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q2_fft.png", dpi=300)
plt.close()

print("Questão 2 executada com sucesso.")