clc;
clear;
close all;

% Parametros
N = 128;
n = 0:N-1;

% Frequencia fundamental
f0 = 0.1;

% Sinal fundamental
x1 = sin(2*pi*f0*n);

% Harmonico (2*f0)
x2 = 0.5*sin(2*pi*2*f0*n);

% Sinal composto
x = x1 + x2;

% FFT
X = fft(x);
magX = abs(X);

f = (0:N-1)/N;

% -------------------------
% Dominio do tempo
% -------------------------
figure(1);
stem(n, x, 'filled');
grid on;
xlabel('n');
ylabel('x[n]');
title('Sinal com harmônicos');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q9_tempo.png', '-dpng');

% -------------------------
% Dominio da frequencia
% -------------------------
figure(2);
stem(f, magX, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('Espectro com harmônicos');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q9_fft.png', '-dpng');