import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, lfilter

# ==========================
# Parâmetros
# ==========================
fs = 1000          # Frequência de amostragem (Hz)
fc = 100           # Frequência de corte (Hz)

# ==========================
# Criação do impulso unitário
# ==========================
N = 100

impulso = np.zeros(N)
impulso[0] = 1

# ==========================
# Filtro FIR
# ==========================
num_taps = 21

h_fir = firwin(num_taps, fc, fs=fs)

resposta_fir = lfilter(h_fir, 1, impulso)

# ==========================
# Filtro IIR Butterworth
# ==========================
ordem = 4

b, a = butter(ordem, fc / (fs / 2), btype='low')

resposta_iir = lfilter(b, a, impulso)

# ==========================
# Gráfico FIR
# ==========================
plt.figure(figsize=(10, 4))

plt.stem(np.arange(N), resposta_fir)

plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Resposta ao impulso - Filtro FIR")

plt.grid(True)

plt.savefig("parte4/resultados/q6_fir_impulso.png",
            dpi=300)

plt.close()

# ==========================
# Gráfico IIR
# ==========================
plt.figure(figsize=(10, 4))

plt.stem(np.arange(N), resposta_iir)

plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Resposta ao impulso - Filtro IIR Butterworth")

plt.grid(True)

plt.savefig("parte4/resultados/q6_iir_impulso.png",
            dpi=300)

plt.close()

print("Questão 6 executada com sucesso.")