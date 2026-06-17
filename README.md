# Estudo Dirigido – Processamento Digital de Sinais (PDS)

##  Descrição

Este repositório contém o desenvolvimento do estudo dirigido da disciplina de **Processamento Digital de Sinais (PDS)**, organizado em etapas progressivas que abordam conceitos fundamentais da área por meio de fundamentação teórica, simulações computacionais e análise dos resultados obtidos.

Atualmente, o projeto está dividido nas seguintes partes:

* **Parte 1:** Sinais discretos e sistemas;
* **Parte 3:** Análise no domínio da frequência;
* **Parte 4:** Filtros digitais.

---

##  Estrutura do repositório

```text
parte1/  → Sinais discretos e sistemas (Python)
parte3/  → Análise espectral (GNU Octave / MATLAB)
parte4/  → Filtros digitais (Python)
```

---

#  Parte 1 – Sinais e Sistemas

Nesta etapa são estudados os conceitos fundamentais de sinais discretos e sistemas lineares invariantes no tempo (LTI).

## Conteúdos abordados

* Impulso unitário;
* Degrau unitário;
* Sinal exponencial;
* Deslocamento temporal;
* Sistemas discretos;
* Memória;
* Linearidade;
* Causalidade;
* Estabilidade;
* Invariância no tempo.

## Ferramentas utilizadas

* Python;
* NumPy;
* Matplotlib.

## Resultados

Os códigos, gráficos e análises encontram-se em:

```text
parte1/
```

---

#  Parte 3 – Análise no Domínio da Frequência

Esta etapa aborda técnicas de representação espectral de sinais discretos.

## Conteúdos abordados

* Transformada Discreta de Fourier (DFT);
* Fast Fourier Transform (FFT);
* Transformada-Z (conceitos teóricos);
* Aliasing;
* Janelamento;
* Resposta em frequência.

## Ferramentas utilizadas

* GNU Octave;
* MATLAB.

## Resultados

Os códigos e gráficos encontram-se em:

```text
parte3/
```

---

#  Parte 4 – Filtros Digitais

Nesta etapa são estudados os principais conceitos relacionados ao projeto e análise de filtros digitais.

## Conteúdos abordados

* Filtros FIR;
* Filtros IIR;
* Resposta ao impulso;
* Resposta em frequência;
* Polos e zeros;
* Resposta de fase;
* Atraso de grupo;
* Estabilidade;
* Aplicações práticas de filtragem digital.

## Ferramentas utilizadas

* Python;
* NumPy;
* SciPy;
* Matplotlib.

## Resultados

Os códigos, gráficos e análises encontram-se em:

```text
parte4/
```

---

#  Como executar

## Parte 1

```bash
python parte1/simulacoes/sinais.py
```

## Parte 3 (GNU Octave)

```octave
run('parte3/simulacoes/q1_fft.m')
```

## Parte 4

```bash
python parte4/simulacoes/q1.py
```

As demais questões podem ser executadas substituindo `q1.py` por `q2.py`, `q3.py`, ..., `q10.py`.

---

#  Objetivo

Desenvolver conhecimentos sobre modelagem de sinais discretos, análise espectral e filtragem digital, relacionando conceitos teóricos com aplicações práticas em engenharia por meio de simulações computacionais.

---

#  Autor

Arthur Augusto de Oliveira Medeiros
