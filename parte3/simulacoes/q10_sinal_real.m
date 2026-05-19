clc;
clear;
close all;

% Parametros
N = 256;
n = 0:N-1;

% Frequencias
f1 = 0.12;
f2 = 0.30;

% Sinal principal (simula "informacao real")
x1 = sin(2*pi*f1*n);

% Harmonica leve
x2 = 0.4*sin(2*pi*f2*n);

% Ruido (simula sensor real)
ruido = 0.6 * randn(1, N);

% Sinal final (realista)
x = x1 + x2 + ruido;

% FFT
X = fft(x);
magX = abs(X);

f = (0:N-1)/N;

% -------------------------
% Tempo
% -------------------------
figure(1);
stem(n, x, 'filled');
grid on;
xlabel('n');
ylabel('x[n]');
title('Sinal real simulado (com ruido)');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q10_tempo.png', '-dpng');

% -------------------------
% Frequencia
% -------------------------
figure(2);
stem(f, magX, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('Espectro do sinal real simulado');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q10_fft.png', '-dpng');