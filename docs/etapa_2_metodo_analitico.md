# Etapa 2 — Definição do método analítico

## 1. Definição da linguagem de programação

A linguagem adotada no projeto é **Python**, escolhida por sua ampla adoção em Ciência de Dados e por oferecer bibliotecas consolidadas para manipulação de dados, análise exploratória, Processamento de Linguagem Natural e Aprendizado de Máquina.

As bibliotecas definidas para o projeto são:
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- scikit-learn
- unidecode
- joblib

Essa definição atende diretamente ao item da Etapa 2 que exige a escolha objetiva dos pacotes da linguagem Python.

## 2. Análise exploratória da base de dados

Após inspeção da base disponibilizada no Kaggle, o projeto adotou como base principal o arquivo `ifood-restaurants-february-2021.csv`.

### 2.1 Caracterização inicial da base principal
- Total de registros: **406,399**
- Total de colunas: **14**
- Registros duplicados identificados: **0**
- Valores ausentes relevantes:
  - `avatar`: **277**
  - `paymentCodes`: **2**
- Principais categorias observadas:
  - Lanches
  - Brasileira
  - Doces & Bolos
  - Pizza
  - Açaí

### 2.2 Campos de interesse para o projeto
Como o foco metodológico é NLP aplicado à análise textual, os campos centrais da modelagem serão:
- `name`
- `category`
- `tags`

Esses atributos serão combinados para compor uma representação textual mais completa do restaurante.

### 2.3 Pontos de EDA previstos nos notebooks
A análise exploratória foi estruturada para investigar:
- formato da base;
- tipos de dados;
- distribuição da variável `rating`;
- quantidade de nulos;
- frequência de categorias;
- distribuição do tamanho dos textos;
- frequência de palavras;
- impacto da limpeza textual sobre os termos mais recorrentes.

## 3. Tratamento da base de dados (preparação e treinamento)

O tratamento definido para a Etapa 2 foi organizado nas seguintes fases:

### 3.1 Seleção de variáveis
Serão utilizadas:
- `name`
- `category`
- `tags`
- `rating`

Variáveis como `delivery_fee`, `delivery_time`, `distance` e `price_range` poderão apoiar a análise exploratória, mas não serão o núcleo da modelagem textual principal.

### 3.2 Regras de limpeza
O pipeline de preparação contempla:
- conversão para minúsculas;
- remoção de acentos;
- remoção de pontuação;
- remoção de caracteres especiais;
- remoção de múltiplos espaços;
- remoção de stopwords em português;
- concatenação dos campos textuais em uma única coluna.

### 3.3 Tratamento dos registros sem nota
Foi identificada grande presença de restaurantes com `rating == 0`. Para não confundir "sem avaliação" com "baixa avaliação", esses registros serão excluídos do conjunto de treinamento supervisionado.

### 3.4 Vetorização
Os textos tratados serão convertidos em atributos numéricos por meio de **TF-IDF**, com possibilidade de uso de unigramas e bigramas.

### 3.5 Divisão entre treino e teste
A base será dividida em:
- 80% treino
- 20% teste

A divisão será estratificada para preservar a proporção das classes.

## 4. Bases teóricas do método

### 4.1 Processamento de Linguagem Natural
O NLP permite transformar texto livre em dados estruturados aptos à modelagem estatística e ao aprendizado de máquina.

### 4.2 TF-IDF
O TF-IDF mede a importância relativa de um termo em um documento considerando também sua frequência no conjunto total de documentos. Isso ajuda a destacar palavras mais discriminativas.

### 4.3 Classificação supervisionada
Na classificação supervisionada, o algoritmo aprende a partir de exemplos rotulados. Neste projeto, o rótulo é derivado da nota do restaurante.

### 4.4 Regressão Logística
A Regressão Logística foi escolhida por ser:
- interpretável;
- eficiente em dados esparsos;
- adequada como linha de base para problemas de classificação textual.

## 5. Definição da acurácia

A variável-alvo será construída da seguinte forma:
- `alta_avaliacao`: `rating >= 4.5`
- `demais`: `rating < 4.5`

A acurácia será calculada por:

```text
acurácia = previsões corretas / total de previsões
```

Além da acurácia, serão avaliadas:
- precisão;
- recall;
- F1-score;
- matriz de confusão.

Essas métricas complementares são importantes porque permitem avaliar melhor o desempenho em cenários com classes desbalanceadas.

## 6. Síntese metodológica

Com isso, a Etapa 2 fica metodologicamente fechada como:

**classificação supervisionada de textos com TF-IDF + Regressão Logística, usando `name`, `category` e `tags` para prever faixas de avaliação dos restaurantes.**
