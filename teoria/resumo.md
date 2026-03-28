# Modelagem de Sinais e Sistemas Discretos

## 1. Introdução

De acordo com Alan V. Oppenheim e Ronald W. Schafer, sinais podem ser definidos como funções que descrevem a variação de uma grandeza física em função de uma ou mais variáveis independentes, geralmente o tempo.

No contexto do Processamento Digital de Sinais (PDS), o interesse está nos sinais em tempo discreto, que são obtidos a partir da amostragem de sinais contínuos, permitindo sua manipulação por sistemas digitais.

---

## 2. Sinais Contínuos e Discretos

Um sinal contínuo é representado por (x(t)), enquanto um sinal discreto é representado por (x[n]), sendo definido apenas em instantes discretos.

Segundo Oppenheim, um sinal discreto pode ser obtido por amostragem uniforme de um sinal contínuo:

$$
x[n] = x(nT)
$$

onde (T) é o período de amostragem.

### Interpretação Física

Esse processo ocorre em sistemas reais de aquisição de dados, como sensores conectados a microcontroladores, onde o sinal analógico é convertido em digital por meio de um conversor A/D.

---

## 3. Representação por Sequências Elementares

Uma ideia central apresentada por Oppenheim é que qualquer sinal discreto pode ser representado como uma combinação de impulsos deslocados:

$$
x[n] = \sum_{k=-\infty}^{\infty} x[k]\delta[n-k]
$$

Essa representação é fundamental para a análise de sistemas.

---

### 3.1 Impulso Unitário

O impulso discreto é definido como:

$$
\delta[n] =
\begin{cases}
1, & n = 0 \
0, & n \neq 0
\end{cases}
$$

Ele funciona como um “bloco básico” para construção de sinais.

---

### 3.2 Degrau Unitário

$$
u[n] =
\begin{cases}
1, & n \geq 0 \
0, & n < 0
\end{cases}
$$

Esse sinal representa uma mudança abrupta em um sistema.

---

### 3.3 Exponenciais Discretas

Segundo a teoria de sistemas lineares, exponenciais da forma:

$$
x[n] = a^n
$$

são soluções fundamentais para sistemas lineares invariantes no tempo (LTI).

---

## 4. Operações com Sinais

As operações fundamentais incluem:

* deslocamento: (x[n-k])
* inversão: (x[-n])
* escalonamento: (a \cdot x[n])

Essas operações permitem modelar atrasos, simetrias e amplificações em sistemas físicos.

---

## 5. Energia e Potência

A energia de um sinal discreto é definida por:

$$
E = \sum_{n=-\infty}^{\infty} |x[n]|^2
$$

A potência média é:

$$
P = \lim_{N \to \infty} \frac{1}{2N+1} \sum_{n=-N}^{N} |x[n]|^2
$$

Segundo Proakis, essa classificação é essencial para determinar o tipo de processamento adequado ao sinal.

---

## 6. Sistemas Discretos

Um sistema discreto é uma transformação que mapeia um sinal de entrada (x[n]) em um sinal de saída (y[n]).

---

### 6.1 Sistemas Lineares e Invariantes no Tempo (LTI)

De acordo com Oppenheim, sistemas LTI são particularmente importantes porque podem ser completamente caracterizados por sua resposta ao impulso.

---

### 6.2 Memória

* Sem memória: saída depende apenas de (x[n])
* Com memória: depende de (x[n-k])

---

### 6.3 Causalidade

Um sistema é causal se:

$$
y[n] \text{ depende apenas de } x[k], \quad k \leq n
$$

Essa propriedade é essencial para implementação física.

---

### 6.4 Estabilidade BIBO

Um sistema é BIBO estável se toda entrada limitada gera saída limitada.

---

### 6.5 Invariância no Tempo

Se uma entrada deslocada gera uma saída igualmente deslocada, o sistema é invariante no tempo.

---

## 7. Aplicações Tecnológicas

Os conceitos apresentados são aplicados em diversas áreas:

* monitoramento de vibração em máquinas;
* sensores térmicos industriais;
* processamento de sinais biomédicos;
* sistemas embarcados;
* telecomunicações digitais.

---

## 8. Conexão com o Problema Norteador

A modelagem de sinais discretos permite representar matematicamente sinais provenientes de sensores reais.

Para garantir o processamento correto, é necessário analisar propriedades como:

* causalidade (implementação física);
* estabilidade (robustez do sistema);
* linearidade (facilidade de análise);
* invariância no tempo (consistência).

---

## 9. Conclusão

Com base nos fundamentos apresentados por Oppenheim, a análise de sinais e sistemas discretos constitui a base para o desenvolvimento de algoritmos de processamento digital, sendo essencial em aplicações modernas de engenharia.
