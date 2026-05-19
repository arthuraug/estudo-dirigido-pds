clc;
clear;
close all;

% Numero de amostras
N = 30;

% Vetor n
n = 0:N-1;

% Resposta ao impulso
h = (0.8).^n;

% Grafico
figure;
stem(n, h, 'filled');
grid on;
xlabel('n');
ylabel('h[n]');
title('Resposta ao impulso do sistema');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q7_resposta_impulso.png', '-dpng');