import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# ==========================
# Parâmetros
# ==========================
fs = 100               # Frequência de amostragem (Hz)
t = np.arange(0, 10, 1/fs)

# ==========================
# Simulação de um sensor
# ==========================
# Sinal lento (por exemplo, temperatura ou umidade)

sinal = 2 + 0.5 * np.sin(2 * np.pi * 0.5 * t)

# Ruído aleatório

np.random.seed(42)

ruido = 0.3 * np.random.randn(len(t))

sinal_ruidoso = sinal + ruido

# ==========================
# Filtro Butterworth passa-baixa
# ==========================
fc = 2          # Hz
ordem = 4

b, a = butter(ordem, fc / (fs / 2), btype="low")

# Utiliza filtfilt para evitar atraso de fase

sinal_filtrado = filtfilt(b, a, sinal_ruidoso)

# ==========================
# Gráfico
# ==========================
plt.figure(figsize=(10, 4))

plt.plot(t, sinal_ruidoso,
         label="Sinal com ruído",
         alpha=0.6)

plt.plot(t, sinal_filtrado,
         label="Sinal filtrado",
         linewidth=2)

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")

plt.title("Suavização de um sinal de sensor")

plt.grid(True)
plt.legend()

plt.savefig(
    "parte4/resultados/q10_sensor.png",
    dpi=300
)

plt.close()

print("Questão 10 executada com sucesso.")