# Questão 1

## Interpretação

A FFT apresentou um pico dominante próximo da frequência normalizada 0.1, correspondente à senoide gerada. Isso mostra que o domínio da frequência permite identificar claramente as componentes espectrais do sinal.

---

# Questão 2

## Interpretação

No domínio do tempo, o sinal resultante apresenta uma forma mais complexa devido à soma das duas senoides. Já no domínio da frequência, a FFT permite identificar claramente as duas frequências presentes no sinal, evidenciando a vantagem da análise espectral para decomposição de sinais compostos.

# Questão 3

## Interpretação

Ao reduzir a taxa de amostragem, o espectro do sinal sofreu distorções, causando o fenômeno de aliasing. Isso ocorre porque a frequência de amostragem tornou-se insuficiente para representar corretamente o sinal original. Como consequência, componentes espectrais passam a aparecer em frequências incorretas, provocando sobreposição e perda de informação.

# Questão 4

## Interpretação

Sem a aplicação da janela, o espectro apresentou maior espalhamento de energia, caracterizando vazamento espectral. Após aplicar a janela de Hamming, o espectro ficou mais concentrado em torno da frequência principal. O janelamento reduz as descontinuidades nas extremidades do sinal finito, melhorando a análise espectral.

# Questão 5

## Interpretação

A presença do ruído dificultou a visualização do comportamento periódico do sinal no domínio do tempo. No entanto, a FFT ainda permitiu identificar a frequência principal da senoide por meio do pico dominante no espectro. Isso mostra como a análise espectral auxilia na separação entre componentes úteis e perturbações presentes em sinais reais.

# Questão 6

## Interpretação

Os resultados obtidos pela implementação manual da DFT foram equivalentes aos produzidos pela função FFT do Octave. A principal diferença está no custo computacional, já que a FFT utiliza algoritmos otimizados capazes de calcular a transformada de forma muito mais eficiente, especialmente para sinais grandes.

# Questão 7

## Interpretação

A resposta ao impulso apresentou comportamento exponencial decrescente, tendendo a zero à medida que n aumenta. Isso indica que o sistema é estável, pois sua resposta permanece limitada ao longo do tempo. Como os valores não crescem indefinidamente, o sistema satisfaz o critério de estabilidade BIBO.

# Questão 8

## Interpretação

O aumento do número de amostras melhorou a resolução espectral da FFT, tornando o pico da frequência principal mais definido. Isso ocorre porque sinais mais longos fornecem maior detalhamento no domínio da frequência, permitindo identificar componentes espectrais com mais precisão.

# Questão 9

## Interpretação

O espectro do sinal revelou a presença de uma frequência fundamental e de um harmônico, evidenciando como a FFT permite identificar componentes periódicas em sinais compostos. Esse tipo de análise é amplamente utilizado no diagnóstico de vibrações mecânicas, pois falhas em máquinas frequentemente geram harmônicos característicos no sinal medido.

# Questão 10

## Interpretação

O sinal analisado apresenta características típicas de dados reais, com presença de ruído e múltiplas componentes espectrais. No domínio da frequência, a FFT permitiu identificar as frequências dominantes mesmo na presença de perturbações. Isso demonstra a importância da análise espectral em aplicações reais, como processamento de sinais de sensores e sistemas de monitoramento.