import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# ==========================
# Parâmetros do sinal
# ==========================
fs = 1000            # Frequência de amostragem (Hz)
t = np.arange(0, 1, 1/fs)

# Duas senoides
f1 = 50              # Frequência baixa
f2 = 200             # Frequência alta

x = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

# ==========================
# Projeto do filtro passa-baixa FIR
# ==========================
fc = 100             # Frequência de corte (Hz)

num_taps = 51

h = firwin(num_taps, fc, fs=fs)

# Aplicação do filtro
y = lfilter(h, 1, x)

# ==========================
# FFT para análise espectral
# ==========================
X = np.fft.fft(x)
Y = np.fft.fft(y)

freq = np.fft.fftfreq(len(t), d=1/fs)

# Considera apenas frequências positivas
mask = freq >= 0

# ==========================
# Gráfico no domínio do tempo
# ==========================
plt.figure(figsize=(10,4))
plt.plot(t, x, label="Sinal original")
plt.plot(t, y, label="Sinal filtrado")
plt.xlim(0, 0.1)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Domínio do tempo")
plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q1_tempo.png", dpi=300)
plt.close()

# ==========================
# Gráfico do espectro
# ==========================
plt.figure(figsize=(10,4))
plt.plot(freq[mask], np.abs(X)[mask], label="Original")
plt.plot(freq[mask], np.abs(Y)[mask], label="Filtrado")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Espectro do sinal")
plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q1_fft.png", dpi=300)
plt.close()

print("Questão 1 executada com sucesso.")
