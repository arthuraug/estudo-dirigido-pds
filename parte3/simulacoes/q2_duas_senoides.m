clc;
clear;
close all;

% Parametros
N = 128;

n = 0:N-1;

% Frequencias normalizadas
f1 = 0.1;
f2 = 0.3;

% Duas senoides
x1 = sin(2*pi*f1*n);
x2 = sin(2*pi*f2*n);

% Soma dos sinais
x = x1 + x2;

% FFT
X = fft(x);
magX = abs(X);

% Eixo de frequencia
f = (0:N-1)/N;

% -------------------------
% Dominio do tempo
% -------------------------
figure(1);
stem(n, x, 'filled');
grid on;
xlabel('n');
ylabel('x[n]');
title('Soma de duas senoides');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q2_tempo.png', '-dpng');

% -------------------------
% Dominio da frequencia
% -------------------------
figure(2);
stem(f, magX, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT da soma de senoides');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q2_fft.png', '-dpng');