# Conformidade com a rubrica de avaliação

Este documento foi criado para mostrar, de forma objetiva, onde cada item da rubrica está contemplado na estrutura do projeto.

## 1. Definição da linguagem de programação
**Como foi atendido**
- linguagem principal definida como Python;
- bibliotecas escolhidas sem deixar itens em aberto.

**Onde aparece**
- `README.md`
- `docs/etapa_2_metodo_analitico.md`
- `requirements.txt`

## 2. Análise exploratória da base de dados
**Como foi atendido**
- notebook exclusivo para EDA;
- descrição da dimensão da base, nulos, duplicidades, categorias e distribuição de rating;
- escolha explícita da base principal.

**Onde aparece**
- `notebooks/01_analise_exploratoria_ifood.ipynb`
- `docs/etapa_2_metodo_analitico.md`
- `data/README.md`

## 3. Tratamento da base de dados
**Como foi atendido**
- pipeline documentado de limpeza textual;
- tratamento de nulos;
- remoção de duplicidades;
- construção da coluna textual consolidada;
- separação entre treino e teste.

**Onde aparece**
- `src/utils_text.py`
- `src/data_preparation.py`
- `src/train_model.py`
- `README.md`

## 4. Definição e descrição das bases teóricas dos métodos
**Como foi atendido**
- justificativa conceitual para NLP;
- explicação do TF-IDF;
- explicação da classificação supervisionada;
- justificativa da Regressão Logística.

**Onde aparece**
- `docs/etapa_2_metodo_analitico.md`
- `README.md`

## 5. Definição e descrição de como será calculada a acurácia
**Como foi atendido**
- fórmula da acurácia apresentada;
- definição da variável-alvo;
- métricas complementares para robustez.

**Onde aparece**
- `docs/etapa_2_metodo_analitico.md`
- `src/evaluate_model.py`
- `notebooks/02_modelagem_nlp_ifood.ipynb`

## 6. Ajustes feitos para manter coerência com a base real
Foram feitas correções importantes para o projeto ficar harmônico:
- substituição de termos genéricos por nomes reais das colunas;
- definição de um método analítico único;
- eliminação da ambiguidade entre clusterização e classificação;
- tratamento explícito dos registros sem avaliação.

## 7. Nível esperado na rubrica
A estrutura foi organizada para se aproximar do nível **Excelente**, pois:
- detalha a metodologia;
- evita inconsistências entre base e documentação;
- mostra preparação clara da base;
- define métricas de avaliação;
- apresenta fluxo reproduzível em notebooks e scripts.
