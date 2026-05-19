clc;
clear;
close all;

% Parametros
N = 128;
n = 0:N-1;

% Frequencia da senoide
f0 = 0.13;

% Sinal original
x = sin(2*pi*f0*n);

% FFT sem janela
X1 = fft(x);
magX1 = abs(X1);

% Janela de Hamming
w = hamming(N)';

% Aplicacao da janela
xw = x .* w;

% FFT com janela
X2 = fft(xw);
magX2 = abs(X2);

% Eixo de frequencia
f = (0:N-1)/N;

% -------------------------
% Sem janela
% -------------------------
figure(1);
stem(f, magX1, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT sem janelamento');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q4_sem_janela.png', '-dpng');

% -------------------------
% Com janela de Hamming
% -------------------------
figure(2);
stem(f, magX2, 'filled');
grid on;
xlabel('Frequencia normalizada');
ylabel('|X[k]|');
title('FFT com janela de Hamming');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q4_com_janela.png', '-dpng');