clc;
clear;
close all;

% Numero de amostras
N = 128;

% Vetor de tempo
n = 0:N-1;

% Frequencia original
f0 = 0.4;

% -------------------------
% Sinal original
% -------------------------
x1 = sin(2*pi*f0*n);

X1 = fft(x1);
magX1 = abs(X1);

f = (0:N-1)/N;

% -------------------------
% Sinal subamostrado
% -------------------------
n2 = 0:2:N-1;

x2 = sin(2*pi*f0*n2);

X2 = fft(x2);
magX2 = abs(X2);

f2 = (0:length(X2)-1)/length(X2);

% -------------------------
% Espectro original
% -------------------------
figure(1);
stem(f, magX1, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('Espectro com amostragem adequada');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q3_fft_original.png', '-dpng');

% -------------------------
% Espectro com aliasing
% -------------------------
figure(2);
stem(f2, magX2, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('Espectro apos reducao da amostragem');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q3_fft_aliasing.png', '-dpng');