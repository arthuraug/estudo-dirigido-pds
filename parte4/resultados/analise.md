# Análise dos Resultados

## Questão 1

Foi gerado um sinal composto por duas senoides de frequências diferentes (50 Hz e 200 Hz) e aplicado um filtro digital passa-baixa. Observou-se que a componente de baixa frequência permaneceu praticamente inalterada, enquanto a componente de alta frequência foi significativamente atenuada. A análise do espectro confirmou que apenas as frequências abaixo da frequência de corte foram preservadas, demonstrando o funcionamento esperado do filtro.

## Questão 2

Foi criado um sinal senoidal contaminado por ruído branco aditivo e aplicado um filtro FIR passa-baixa. Após a filtragem, verificou-se uma redução significativa das componentes de alta frequência responsáveis pelo ruído, tornando o sinal mais suave e próximo do original. O resultado evidencia a eficiência dos filtros FIR na melhoria da qualidade de sinais provenientes de sensores e sistemas de aquisição de dados.

## Questão 3

O experimento anterior foi repetido utilizando um filtro IIR Butterworth. A filtragem também reduziu consideravelmente o ruído presente no sinal, preservando sua componente principal. Comparando com o filtro FIR, observou-se que o filtro IIR alcançou desempenho semelhante utilizando uma ordem menor, reduzindo o custo computacional, embora apresente resposta de fase não linear.

## Questão 4

Foram comparadas as respostas em frequência de filtros FIR e IIR com frequências de corte semelhantes. O filtro IIR apresentou uma transição mais abrupta entre as bandas de passagem e rejeição, enquanto o filtro FIR apresentou uma resposta mais gradual. Em contrapartida, o filtro FIR pode oferecer fase linear, característica importante em aplicações que exigem preservação da forma temporal do sinal.

## Questão 5

Foi construído o mapa de polos e zeros de um filtro IIR Butterworth. Observou-se que todos os polos permaneceram localizados no interior do círculo unitário do plano-Z, garantindo a estabilidade do sistema. A análise confirma a relação direta entre a posição dos polos e o comportamento estável dos filtros digitais.

## Questão 6

A resposta ao impulso do filtro FIR apresentou duração finita, tornando-se nula após um número limitado de amostras. Já o filtro IIR apresentou uma resposta que decai progressivamente ao longo do tempo, permanecendo teoricamente infinita devido à presença de realimentação. Essa comparação ilustra claramente a principal diferença estrutural entre filtros FIR e IIR.

## Questão 7

Foi projetado um filtro passa-faixa para selecionar uma componente específica presente em um sinal composto por três senoides. Após a filtragem, verificou-se que apenas a frequência localizada dentro da faixa especificada permaneceu praticamente preservada, enquanto as demais foram fortemente atenuadas. O resultado demonstra a capacidade dos filtros passa-faixa de isolar componentes espectrais de interesse.

## Questão 8

A comparação entre as respostas de fase mostrou que o filtro FIR apresenta comportamento aproximadamente linear na banda de passagem, preservando melhor a forma temporal do sinal. O filtro IIR Butterworth, por outro lado, apresentou fase não linear, podendo introduzir diferentes atrasos para cada componente de frequência e causar distorções temporais.

## Questão 9

Foi analisado o atraso de grupo dos filtros FIR e IIR. O filtro FIR apresentou atraso praticamente constante ao longo da banda de passagem, característica associada à fase linear. Já o filtro IIR apresentou atraso variável em função da frequência. Esse comportamento evidencia a importância do atraso de grupo em sistemas de comunicação e processamento digital, nos quais a preservação da estrutura temporal do sinal é fundamental.

## Questão 10

Foi implementada uma aplicação prática envolvendo a suavização de um sinal de sensor contaminado por ruído branco. A utilização de um filtro digital Butterworth permitiu reduzir significativamente as oscilações de alta frequência sem comprometer a tendência principal do sinal. Esse resultado demonstra como técnicas de filtragem digital podem melhorar a confiabilidade das medições em aplicações de monitoramento ambiental, sistemas embarcados e Internet das Coisas (IoT).



## Problema Norteador (Metodologia PBL)

Em um sistema de monitoramento agrícola, os sensores utilizados para medir variáveis ambientais, como temperatura, umidade e umidade do solo, estão sujeitos à presença de ruídos provenientes do ambiente, interferências eletromagnéticas e imperfeições dos circuitos eletrônicos. Essas perturbações podem comprometer a qualidade das medições e levar a decisões incorretas por parte dos sistemas de controle.

Uma forma de minimizar esse problema consiste no projeto e na aplicação de filtros digitais adequados às características do sinal de interesse. Inicialmente, é necessário analisar o conteúdo espectral do sinal para identificar quais componentes representam a informação útil e quais correspondem ao ruído ou às interferências. A partir dessa análise, pode-se selecionar um filtro apropriado, como um filtro passa-baixa para eliminar componentes de alta frequência ou um filtro passa-faixa para isolar frequências específicas.

Durante o projeto, também devem ser considerados aspectos como estabilidade, resposta em frequência, resposta de fase, atraso de grupo e custo computacional. Filtros FIR oferecem estabilidade inerente e possibilidade de fase linear, preservando melhor a forma do sinal, enquanto filtros IIR normalmente apresentam maior eficiência computacional e conseguem atingir especificações semelhantes utilizando ordens menores.

A validação do filtro pode ser realizada por meio de simulações computacionais, comparação entre os sinais antes e depois da filtragem e análise de seus espectros de frequência. Caso a filtragem preserve as componentes relevantes do sinal e reduza significativamente o ruído presente nas medições, o sistema torna-se mais confiável para aplicações de monitoramento agrícola e tomada automática de decisões.

Dessa forma, o projeto adequado de filtros digitais permite melhorar a qualidade das informações obtidas pelos sensores, reduzindo interferências sem comprometer os dados relevantes necessários para o funcionamento eficiente do sistema.
