import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# ==========================
# Parâmetros
# ==========================
fs = 1000                      # Frequência de amostragem (Hz)
t = np.arange(0, 1, 1/fs)

# ==========================
# Sinal composto
# ==========================
f1 = 50
f2 = 150
f3 = 300

x = (
    np.sin(2 * np.pi * f1 * t)
    + np.sin(2 * np.pi * f2 * t)
    + np.sin(2 * np.pi * f3 * t)
)

# ==========================
# Filtro passa-faixa Butterworth
# ==========================
ordem = 4

faixa = [120, 180]

b, a = butter(
    ordem,
    [faixa[0] / (fs / 2), faixa[1] / (fs / 2)],
    btype="bandpass"
)

# Filtragem
y = lfilter(b, a, x)

# ==========================
# FFT
# ==========================
X = np.fft.fft(x)
Y = np.fft.fft(y)

freq = np.fft.fftfreq(len(t), d=1/fs)

mask = freq >= 0

# ==========================
# Gráfico do espectro
# ==========================
plt.figure(figsize=(10, 4))

plt.plot(freq[mask], np.abs(X)[mask], label="Original")
plt.plot(freq[mask], np.abs(Y)[mask], label="Filtrado")

plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Filtro Passa-Faixa")

plt.grid(True)
plt.legend()

plt.savefig(
    "parte4/resultados/q7_fft.png",
    dpi=300
)

plt.close()

print("Questão 7 executada com sucesso.")