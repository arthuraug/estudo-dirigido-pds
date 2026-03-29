#  Estudo Dirigido – Processamento Digital de Sinais (PDS)

##  Descrição

Este repositório contém o desenvolvimento da Parte 1 do estudo dirigido da disciplina de Processamento Digital de Sinais (PDS), abordando a modelagem de sinais discretos e a análise de sistemas.

O projeto integra fundamentos teóricos, simulações computacionais em Python e interpretação de resultados.

---

##  Conteúdos abordados

* Sinais discretos (impulso, degrau, exponencial)
* Operações com sinais (deslocamento)
* Sistemas discretos
* Classificação de sistemas:

  * memória
  * linearidade
  * causalidade
  * estabilidade
  * invariância no tempo

---

##  Simulações

As simulações foram implementadas em Python utilizando as bibliotecas:

* NumPy
* Matplotlib

Os seguintes sinais e sistemas foram analisados:

* Impulso unitário
* Degrau unitário
* Sinal exponencial
* Deslocamento no tempo
* Sistema: y[n] = x[n] + x[n-1]

---

##  Resultados

Os gráficos gerados estão disponíveis na pasta:

```bash
/resultados
```

A análise dos resultados pode ser encontrada em:

```bash
/resultados/analise.md
```

---

##  Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/arthuraug/estudo-dirigido-pds.git
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar as simulações

```bash
python simulacoes/sinais.py
```

---

##  Objetivo

Modelar sinais discretos, analisar sistemas digitais e relacionar conceitos teóricos com aplicações práticas em engenharia.

---

## 👨‍💻 Autor

Arthur Augusto de Oliveira Medeiros
