import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# ==========================
# Parâmetros
# ==========================
fs = 1000                    # Frequência de amostragem (Hz)
t = np.arange(0, 1, 1/fs)

# ==========================
# Sinal original
# ==========================
f = 50                       # Frequência da senoide (Hz)
sinal = np.sin(2 * np.pi * f * t)

# ==========================
# Ruído branco
# ==========================
np.random.seed(42)

ruido = 0.5 * np.random.randn(len(t))

sinal_ruidoso = sinal + ruido

# ==========================
# Filtro IIR Butterworth
# ==========================
fc = 100                     # Frequência de corte (Hz)

ordem = 4

b, a = butter(ordem, fc / (fs / 2), btype='low')

# Aplicação do filtro
sinal_filtrado = lfilter(b, a, sinal_ruidoso)

# ==========================
# Domínio do tempo
# ==========================
plt.figure(figsize=(10,4))

plt.plot(t, sinal_ruidoso, label="Sinal com ruído")
plt.plot(t, sinal_filtrado, label="Filtrado (Butterworth)", linewidth=2)

plt.xlim(0, 0.1)

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Filtro IIR Butterworth")

plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q3_tempo.png", dpi=300)
plt.close()

# ==========================
# FFT
# ==========================
X = np.fft.fft(sinal_ruidoso)
Y = np.fft.fft(sinal_filtrado)

freq = np.fft.fftfreq(len(t), d=1/fs)

mask = freq >= 0

plt.figure(figsize=(10,4))

plt.plot(freq[mask], np.abs(X)[mask], label="Com ruído")
plt.plot(freq[mask], np.abs(Y)[mask], label="Filtrado")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Espectro após filtro IIR Butterworth")

plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q3_fft.png", dpi=300)
plt.close()

print("Questão 3 executada com sucesso.")