# Resultados e Análise das Simulações

## 1. Impulso Unitário δ[n]

O gráfico do impulso unitário apresenta valor igual a 1 apenas no instante n = 0 e zero nos demais pontos. Esse comportamento caracteriza um sinal discreto de curta duração, utilizado como base para a representação de sinais mais complexos.

Do ponto de vista físico, o impulso pode representar um evento instantâneo, como um pulso elétrico aplicado a um sistema.

---

## 2. Degrau Unitário u[n]

O sinal degrau apresenta valor nulo para n < 0 e valor constante igual a 1 para n ≥ 0. Esse tipo de sinal modela situações em que um sistema é ativado e permanece em funcionamento.

Fisicamente, pode representar o acionamento de um dispositivo, como o início da operação de um motor ou sistema eletrônico.

---

## 3. Deslocamento no Tempo

O deslocamento do sinal evidencia a operação de atraso, onde o sinal original é deslocado no eixo do tempo. No caso analisado, foi aplicado um atraso de 3 unidades.

Esse comportamento está diretamente relacionado a fenômenos reais, como o tempo de resposta de sensores ou atrasos em sistemas de comunicação.

---

## 4. Sistema Discreto: y[n] = x[n] + x[n-1]

O sistema analisado combina o valor atual do sinal de entrada com seu valor imediatamente anterior, caracterizando um sistema com memória.

### Classificação do sistema:

* **Memória:** possui memória, pois depende de x[n-1];
* **Linearidade:** é linear, pois satisfaz o princípio da superposição;
* **Causalidade:** é causal, pois depende apenas de valores presentes e passados;
* **Estabilidade:** é estável no sentido BIBO, pois entradas limitadas produzem saídas limitadas;
* **Invariância no tempo:** é invariante, pois seu comportamento não depende do instante de aplicação do sinal.

---

## 5. Sinal Exponencial

O sinal exponencial discreto apresentou comportamento de decaimento ao longo do tempo, devido ao valor de a = 0.8.

Esse tipo de sinal é frequentemente associado a fenômenos físicos como dissipação de energia, resfriamento térmico e descarga de capacitores.

---

## 6. Conexão com Aplicações Reais

As simulações realizadas demonstram como sinais discretos podem representar fenômenos físicos reais e como sistemas digitais processam essas informações.

A análise das propriedades dos sistemas é essencial para garantir sua implementação prática, especialmente em aplicações como sensores industriais, sistemas embarcados e processamento digital em tempo real.

---

## 7. Conclusão

Os resultados obtidos evidenciam a importância da modelagem de sinais discretos e da análise de sistemas para o desenvolvimento de soluções tecnológicas confiáveis. A utilização de ferramentas computacionais permitiu validar os conceitos teóricos estudados, estabelecendo uma conexão direta entre teoria e prática.
