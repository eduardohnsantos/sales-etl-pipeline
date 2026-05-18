# Multi-Store Sales ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![MkDocs](https://img.shields.io/badge/Docs-MkDocs-green)

Pipeline ETL para consolidação de vendas multi-lojas utilizando Python, Pandas, Poetry e MkDocs.

---

# Arquitetura do Pipeline

```mermaid
flowchart LR

A[Excel Files - Raw Layer] --> B[Extract]
B --> C[extract_from_excel]

C --> D[Transform]
D --> E[Concatenação]
E --> F[Tratamento]
F --> G[Remoção de Duplicados]

G --> H[Load]
H --> I[Trusted Layer]

I --> J[vendas_consolidadas.xlsx]
```

---

# Fluxo ETL

## Extract
Responsável por:
- ler múltiplos arquivos Excel
- capturar dados da camada raw
- transformar arquivos em DataFrames

---

## Transform
Responsável por:
- concatenar os DataFrames
- remover registros duplicados
- padronizar informações
- consolidar os dados

---

## Load
Responsável por:
- salvar os dados tratados
- persistir a camada trusted
- gerar o arquivo consolidado

---

# Estrutura do Projeto

```text
sales-etl-pipeline/
│
├── data/
│   ├── raw/
│   ├── trusted/
│   └── error/
│
├── docs/
│
├── src/
│   ├── pipeline/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   │
│   ├── tests/
│   └── main.py
│
├── .pre-commit-config.yaml
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

---

# Stack Utilizada

- Python
- Pandas
- OpenPyXL
- Poetry
- Pytest
- MkDocs
- Mermaid
- Pre-commit
- Black
- Flake8
- Isort
- Pydocstyle

---

# Camadas de Dados

| Camada | Descrição |
|---|---|
| Raw | Dados brutos recebidos |
| Trusted | Dados tratados e consolidados |
| Error | Dados com falha no processamento |

---

# Como Executar

## Clonar repositório

```bash
git clone https://github.com/eduardohnsantos/sales-etl-pipeline.git
```

---

## Instalar dependências

```bash
poetry install
```

---

## Executar pipeline

```bash
poetry run python src/main.py
```

---

## Executar testes

```bash
pytest -v
```

---

## Executar documentação

```bash
mkdocs serve
```

---

# Qualidade de Código

O projeto utiliza:

- Black para formatação
- Isort para organização de imports
- Flake8 para lint
- Pydocstyle para padronização de docstrings
- Pre-commit para automação de validações

---

# Testes

Os testes unitários foram implementados utilizando Pytest para garantir:

- consolidação correta dos DataFrames
- validação da transformação
- qualidade do pipeline

---

# Função de Extração (`extract.py`)

::: pipeline.extract.extract_from_excel

---

# Função de Transformação (`transform.py`)

::: pipeline.transform.contact_data_frames

---

# Função de Load (`load.py`)

::: pipeline.load.load_excel

---

# Melhorias Futuras

- Agendamento automático com Apache Airflow
- Persistência em PostgreSQL
- Deploy em Cloud
- Integração com Power BI
- Monitoramento e logs
- Orquestração com Docker
- Camada Gold para analytics
