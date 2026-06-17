import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, group_delay

# ==========================
# Parâmetros
# ==========================
fs = 1000          # Frequência de amostragem (Hz)
fc = 100           # Frequência de corte (Hz)

# ==========================
# Filtro FIR
# ==========================
num_taps = 51

coef_fir = firwin(num_taps, fc, fs=fs)

# ==========================
# Filtro IIR Butterworth
# ==========================
ordem = 4

b, a = butter(ordem, fc / (fs / 2), btype='low')

# ==========================
# Atraso de grupo
# ==========================
w_fir, gd_fir = group_delay((coef_fir, 1), fs=fs)

w_iir, gd_iir = group_delay((b, a), fs=fs)

# ==========================
# Gráfico
# ==========================
plt.figure(figsize=(10, 5))

plt.plot(w_fir, gd_fir, label="FIR")
plt.plot(w_iir, gd_iir, label="IIR Butterworth")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Atraso de grupo (amostras)")
plt.title("Comparação do atraso de grupo")

plt.grid(True)
plt.legend()

plt.savefig(
    "parte4/resultados/q9_group_delay.png",
    dpi=300
)

plt.close()

print("Questão 9 executada com sucesso.")