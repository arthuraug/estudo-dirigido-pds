clc;
clear;
close all;

% Sinal curto
x = [1 2 1 0];

% Numero de amostras
N = length(x);

% -------------------------
% DFT manual
% -------------------------
X_manual = zeros(1, N);

for k = 0:N-1
    soma = 0;

    for n = 0:N-1
        soma = soma + x(n+1) * exp(-1j*2*pi*k*n/N);
    end

    X_manual(k+1) = soma;
end

% -------------------------
% FFT do Octave
% -------------------------
X_fft = fft(x);

% Exibicao
disp('Resultado da DFT manual:');
disp(X_manual);

disp('Resultado da FFT:');
disp(X_fft);

% -------------------------
% Grafico
% -------------------------
figure;
stem(0:N-1, abs(X_manual), 'filled');
grid on;
xlabel('k');
ylabel('|X[k]|');
title('Magnitude da DFT manual');

print('C:/Users/Pichau/estudo-dirigido-pds/parte3/resultados/q6_dft_manual.png', '-dpng');