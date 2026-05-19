clc;
clear;
close all;

% Frequencia da senoide
f0 = 0.15;

% -------------------------
% Sinal curto
% -------------------------
N1 = 32;
n1 = 0:N1-1;

x1 = sin(2*pi*f0*n1);

X1 = fft(x1);
magX1 = abs(X1);

f1 = (0:N1-1)/N1;

% -------------------------
% Sinal longo
% -------------------------
N2 = 128;
n2 = 0:N2-1;

x2 = sin(2*pi*f0*n2);

X2 = fft(x2);
magX2 = abs(X2);

f2 = (0:N2-1)/N2;

% -------------------------
% FFT sinal curto
% -------------------------
figure(1);
stem(f1, magX1, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT com poucas amostras');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q8_fft_curta.png', '-dpng');

% -------------------------
% FFT sinal longo
% -------------------------
figure(2);
stem(f2, magX2, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT com mais amostras');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q8_fft_longa.png', '-dpng');