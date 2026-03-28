# Modelagem de Sinais e Sistemas Discretos

## 1. Introdução

Os sinais são formas de representar fenômenos físicos ao longo do tempo. No contexto da engenharia, eles permitem descrever grandezas como temperatura, pressão, vibração e tensão elétrica. Já os sistemas são responsáveis por processar esses sinais, produzindo uma saída a partir de uma entrada.

No processamento digital de sinais, trabalha-se principalmente com sinais discretos, que são obtidos a partir da amostragem de sinais contínuos.

---

## 2. Sinais Contínuos e Discretos

Um **sinal contínuo** é definido para todos os instantes de tempo, sendo representado por uma função ( x(t) ).

Exemplo:

* Temperatura ao longo do tempo
* Sinal analógico de áudio

Um **sinal discreto** é definido apenas em instantes específicos, geralmente obtidos por amostragem:

[
x[n] = x(nT)
]

onde ( T ) é o período de amostragem.

Exemplo:

* Leitura digital de um sensor
* Áudio digital

---

## 3. Sequências Elementares

### 3.1 Impulso Unitário

O impulso discreto é definido por:

[
\delta[n] =
\begin{cases}
1, & n = 0 \
0, & n \neq 0
\end{cases}
]

Ele é utilizado para representar sistemas e construir outros sinais.

---

### 3.2 Degrau Unitário

O degrau unitário é definido como:

[
u[n] =
\begin{cases}
1, & n \geq 0 \
0, & n < 0
\end{cases}
]

Esse sinal representa o “ligar” de um sistema.

---

### 3.3 Exponencial Discreta

Um sinal exponencial pode ser representado por:

[
x[n] = a^n
]

Dependendo do valor de ( a ), o sinal pode crescer ou decair ao longo do tempo.

---

## 4. Operações com Sinais

### 4.1 Deslocamento no Tempo

O deslocamento altera a posição do sinal no tempo:

* ( x[n - k] ): atraso
* ( x[n + k] ): avanço

---

### 4.2 Inversão Temporal

Consiste em inverter o sinal no tempo:

[
x[-n]
]

---

### 4.3 Escalonamento

Multiplica o sinal por uma constante:

[
y[n] = a \cdot x[n]
]

---

## 5. Energia e Potência

A energia de um sinal discreto é dada por:

[
E = \sum_{n=-\infty}^{\infty} |x[n]|^2
]

A potência média é:

[
P = \lim_{N \to \infty} \frac{1}{2N+1} \sum_{n=-N}^{N} |x[n]|^2
]

* Sinais com energia finita são chamados de **sinais de energia**
* Sinais com potência finita são chamados de **sinais de potência**

---

## 6. Sistemas Discretos

Um sistema discreto transforma um sinal de entrada ( x[n] ) em uma saída ( y[n] ).

### 6.1 Sistemas com e sem memória

* **Sem memória**: saída depende apenas de ( x[n] )
* **Com memória**: depende de valores passados ou futuros

---

### 6.2 Linearidade

Um sistema é linear se satisfaz:

* Princípio da superposição
* Homogeneidade

---

### 6.3 Causalidade

* **Causal**: depende apenas do presente ou passado
* **Não causal**: depende do futuro

---

### 6.4 Invariância no Tempo

Um sistema é invariante no tempo se seu comportamento não muda ao longo do tempo.

---

### 6.5 Estabilidade (BIBO)

Um sistema é estável se toda entrada limitada produz uma saída limitada.

---

### 6.6 Invertibilidade

Um sistema é invertível se é possível recuperar a entrada a partir da saída.

---

## 7. Aplicações em Engenharia

Os conceitos de sinais e sistemas discretos são amplamente aplicados em:

* Monitoramento de vibração em máquinas
* Sensores de temperatura em processos industriais
* Sistemas digitais embarcados
* Processamento de sinais elétricos
* Controle de velocidade de motores

---

## 8. Conclusão

A modelagem de sinais discretos permite representar matematicamente fenômenos reais, possibilitando seu processamento em sistemas digitais. A análise das propriedades dos sistemas é essencial para garantir funcionamento correto, previsível e estável, sendo fundamental em diversas aplicações da engenharia.

