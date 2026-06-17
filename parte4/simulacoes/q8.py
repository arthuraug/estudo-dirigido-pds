import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, freqz

# ==========================
# Parâmetros
# ==========================
fs = 1000          # Frequência de amostragem (Hz)
fc = 100           # Frequência de corte (Hz)

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

# Fase desembrulhada (evita saltos de ±π)
fase_fir = np.unwrap(np.angle(h_fir))
fase_iir = np.unwrap(np.angle(h_iir))

# ==========================
# Gráfico
# ==========================
plt.figure(figsize=(10, 5))

plt.plot(w_fir, fase_fir, label="FIR")
plt.plot(w_iir, fase_iir, label="IIR Butterworth")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Fase (rad)")
plt.title("Comparação da resposta de fase")

plt.grid(True)
plt.legend()

plt.savefig(
    "parte4/resultados/q8_fase.png",
    dpi=300
)

plt.close()

print("Questão 8 executada com sucesso.")