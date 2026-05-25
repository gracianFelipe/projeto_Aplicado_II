# Pasta `data/`

Esta pasta organiza os dados brutos e os dados preparados do projeto.

## Estrutura

```text
data/
├── raw/
└── processed/
```

## 1. Dados brutos (`raw/`)

Nesta pasta devem ser armazenados os arquivos originais do dataset do Kaggle:

- `ifood-restaurants-february-2021.csv`
- `ifood-restaurants-november-2020.csv`

### Motivo da escolha da base principal
A base de fevereiro de 2021 foi definida como base principal porque possui mais variáveis úteis para a proposta analítica:
- `availableForScheduling`
- `category`
- `delivery_fee`
- `delivery_time`
- `distance`
- `ibge`
- `minimumOrderValue`
- `name`
- `paymentCodes`
- `price_range`
- `rating`
- `tags`
- `url`

## 2. Dados processados (`processed/`)

Arquivos esperados após o tratamento:
- `ifood_feb2021_text_base.parquet`
- `ifood_train.csv`
- `ifood_test.csv`
- `metrics.json`

## 3. Dicionário resumido da base principal

| Coluna | Tipo geral | Uso no projeto |
|---|---|---|
| `name` | texto | principal fonte textual |
| `category` | texto | categoria do restaurante |
| `tags` | texto | metadados textuais complementares |
| `rating` | numérico | criação da variável-alvo |
| `price_range` | categórico | possível apoio exploratório |
| `delivery_time` | numérico | apoio exploratório |
| `delivery_fee` | numérico | apoio exploratório |
| `distance` | numérico | apoio exploratório |
| `paymentCodes` | texto | opcional para análises futuras |
| `url` | texto | identificação e rastreabilidade |

## 4. Ajuste metodológico importante

A documentação inicial do projeto mencionava "segmentos" e "descrições". Na base real do Kaggle, esses campos não aparecem de forma explícita. Para manter a coerência metodológica, o projeto passa a trabalhar com:
- `name`
- `category`
- `tags`

## 5. Boas práticas

- não versionar arquivos muito grandes diretamente no Git sem necessidade;
- manter os dados brutos inalterados;
- salvar a base tratada em `processed/`;
- registrar no relatório toda decisão de limpeza e transformação.
