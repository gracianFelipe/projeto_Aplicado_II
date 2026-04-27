# Projeto Aplicado II — Análise NLP em Dados do iFood

Este repositório foi reorganizado para a **Etapa A2 — Definição do método analítico**, mantendo coerência com a proposta da Etapa A1 e com a rubrica de avaliação da disciplina.

## 1. Objetivo do projeto

Desenvolver um **modelo supervisionado de classificação de textos** para analisar padrões presentes nos nomes e nas categorias dos restaurantes do iFood, buscando relacionar esses padrões com a avaliação do estabelecimento.

A proposta original do grupo falava em "categorias, segmentos e nomes". Após a conferência da base real, o termo **segmentos** foi ajustado para os campos textuais efetivamente disponíveis no dataset:
- `name`
- `category`
- `tags`

Esse ajuste mantém o projeto harmônico com a base escolhida e evita inconsistências entre documentação e dados reais.

## 2. Base de dados utilizada

Dataset público do Kaggle: **iFood Restaurants Data**.

Arquivos disponibilizados:
- `ifood-restaurants-february-2021.csv`
- `ifood-restaurants-november-2020.csv`

### Base principal adotada na Etapa A2
A base principal do projeto será `ifood-restaurants-february-2021.csv`, pois ela é mais rica para a proposta analítica e possui:
- **406,399 registros**
- **14 colunas**
- colunas textuais relevantes como `name`, `category`, `tags` e `paymentCodes`

A base `ifood-restaurants-november-2020.csv` poderá ser usada como apoio comparativo, mas não será a base central da modelagem nesta etapa.

## 3. Linguagem e bibliotecas definidas

A linguagem oficial do projeto é **Python**.

Bibliotecas definidas:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `nltk`
- `scikit-learn`
- `unidecode`
- `joblib`
- `ipykernel`

Essas bibliotecas atendem aos cinco pontos cobrados na Etapa A2:
1. definição da linguagem;
2. análise exploratória;
3. tratamento da base;
4. base teórica do método;
5. cálculo da acurácia.

## 4. Método analítico escolhido

O projeto foi refinado para usar um método único e bem definido:

**Classificação supervisionada de textos com TF-IDF + Regressão Logística**

### Justificativa
Essa escolha deixa o projeto mais forte na rubrica porque:
- define um método analítico claro;
- combina bem com o foco em NLP;
- permite explicar objetivamente como a acurácia será calculada;
- usa um modelo interpretável e adequado para dados textuais vetorizados.

## 5. Estratégia analítica

### 5.1 Análise exploratória da base
A EDA prevista no projeto contempla:
- dimensão da base;
- tipos de dados;
- valores ausentes;
- duplicidades;
- distribuição da variável `rating`;
- categorias mais frequentes;
- inspeção das colunas textuais;
- análise do tamanho dos textos;
- frequência de termos antes e depois da limpeza.

### 5.2 Tratamento da base
O tratamento definido para a etapa inclui:
- remoção de duplicidades;
- tratamento de nulos;
- padronização textual;
- remoção de acentos;
- remoção de pontuação;
- remoção de stopwords;
- concatenação de `name`, `category` e `tags` em uma coluna textual única;
- vetorização por **TF-IDF**;
- separação treino/teste com estratificação.

### 5.3 Variável-alvo
Como a variável `rating` é numérica contínua e há muitos registros com nota zero, o projeto adotará a seguinte regra para a modelagem supervisionada:
- excluir registros com `rating == 0` da etapa de treinamento;
- criar uma variável binária:
  - `alta_avaliacao` para restaurantes com `rating >= 4.5`
  - `demais` para restaurantes com `rating < 4.5`

Essa decisão melhora a consistência analítica e evita misturar restaurantes sem avaliação com restaurantes efetivamente mal avaliados.

## 6. Como a acurácia será calculada

A acurácia será calculada pela fórmula:

```text
acurácia = previsões corretas / total de previsões
```

Além da acurácia, o projeto também apresentará:
- precisão;
- recall;
- F1-score;
- matriz de confusão.

Isso fortalece a justificativa metodológica e evita depender de uma única métrica.

## 7. Estrutura do repositório

```text
.
├── data/
│   ├── processed/
│   │   └── .gitkeep
│   ├── raw/
│   │   └── .gitkeep
│   └── README.md
├── notebooks/
│   ├── 01_analise_exploratoria_ifood.ipynb
│   └── 02_modelagem_nlp_ifood.ipynb
├── src/
│   ├── _init_.py
│   ├── config.py
│   ├── data_preparation.py
│   ├── evaluate_model.py
│   ├── extract_terms.py
│   ├── train_model.py
│   └── utils_text.py
├── docs/
│   ├── conformidade_rubrica.md
│   └── etapa_2_metodo_analitico.md
├── models/
│   └── ifood_text_classifier.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

## 8. Como usar

### 8.1 Instalação
```bash
pip install -r requirements.txt
```

### 8.2 Organização dos dados
Baixe os arquivos do Kaggle e coloque em:
```text
data/raw/
- `ifood-restaurants-february-2021.csv`
- `ifood-restaurants-november-2020.csv`
```
Se atente que os arquivos não podem estar em pastas

### 8.3 Execução sugerida
```bash
python -m src.data_preparation
python -m src.train_model
python -m src.evaluate_model
```

### 8.4 Exploração em notebook
Os notebooks foram organizados para:
- documentar a análise exploratória;
- demonstrar o fluxo de preparação;
- registrar o treinamento do modelo;
- facilitar a transformação do conteúdo em relatório técnico.

## 9. Observações importantes para manter o projeto harmônico

- O README antigo mencionava bibliotecas ainda "a definir"; isso foi corrigido aqui.
- O foco metodológico foi fechado em **classificação supervisionada**, evitando ambiguidade entre classificação e clusterização.
- A documentação agora usa apenas colunas que realmente existem na base.
- A estrutura foi pensada para atender diretamente aos critérios da rubrica da Etapa 2.

## 10. Equipe

Felipe Graciano
André Cavina
Diogo Ferreira 
