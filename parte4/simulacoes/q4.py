import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, freqz

# ==========================
# Parâmetros
# ==========================
fs = 1000              # Frequência de amostragem (Hz)
fc = 100               # Frequência de corte (Hz)

# ==========================
# Filtro FIR
# ==========================
num_taps = 51

fir_coef = firwin(num_taps, fc, fs=fs)

# ==========================
# Filtro IIR Butterworth
# ==========================
ordem = 4

b, a = butter(ordem, fc / (fs / 2), btype='low')

# ==========================
# Resposta em frequência
# ==========================
w_fir, h_fir = freqz(fir_coef, worN=2048, fs=fs)

w_iir, h_iir = freqz(b, a, worN=2048, fs=fs)

# ==========================
# Gráfico
# ==========================
plt.figure(figsize=(10, 5))

plt.plot(w_fir, 20 * np.log10(np.abs(h_fir) + 1e-10),
         label="FIR")

plt.plot(w_iir, 20 * np.log10(np.abs(h_iir) + 1e-10),
         label="IIR Butterworth")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Comparação das respostas em frequência")

plt.grid(True)
plt.legend()

plt.savefig("parte4/resultados/q4_resposta_frequencia.png",
            dpi=300)

plt.close()

print("Questão 4 executada com sucesso.")