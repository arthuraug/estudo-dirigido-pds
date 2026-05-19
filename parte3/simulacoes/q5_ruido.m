clc;
clear;
close all;

% Parametros
N = 128;
n = 0:N-1;

% Frequencia da senoide
f0 = 0.15;

% Senoide principal
x = sin(2*pi*f0*n);

% Ruido aleatorio
ruido = 0.5 * randn(1, N);

% Sinal com ruido
xr = x + ruido;

% FFT
X = fft(xr);
magX = abs(X);

% Eixo de frequencia
f = (0:N-1)/N;

% -------------------------
% Sinal no tempo
% -------------------------
figure(1);
stem(n, xr, 'filled');
grid on;
xlabel('n');
ylabel('x[n]');
title('Sinal com ruido');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q5_sinal_ruido.png', '-dpng');

% -------------------------
% FFT
% -------------------------
figure(2);
stem(f, magX, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT do sinal com ruido');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q5_fft_ruido.png', '-dpng');