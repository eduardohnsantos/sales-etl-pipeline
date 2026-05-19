# 🚀 Sales ETL Pipeline

<p align="center">
  <img src="./docs/assets/sales-etl-pipeline-banner.png" alt="Sales ETL Pipeline Banner">
</p>

## 📌 Sobre o Projeto

O **Sales ETL Pipeline** é um projeto desenvolvido em Python com foco em Engenharia de Dados, simulando um pipeline ETL utilizado em ambientes corporativos.

O projeto realiza:
- Extração de múltiplos arquivos Excel
- Consolidação de dados
- Tratamento e remoção de duplicidades
- Geração da camada Trusted
- Testes automatizados
- Documentação técnica com MkDocs

---

## 🏗️ Arquitetura do Projeto

```text
data/
├── raw/        # Dados brutos
├── trusted/    # Dados tratados
└── error/      # Logs e falhas

src/
├── pipeline/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   └── test_pipeline.py
│
└── main.py
```

---

## ⚙️ Stack Utilizada

- Python
- Pandas
- Pytest
- Poetry
- MkDocs
- Mermaid
- Pre-commit
- Black
- Isort
- Flake8

---

## ▶️ Executando o Projeto

### Instalar dependências

```bash
poetry install
```

### Executar pipeline

```bash
poetry run python src/main.py
```

### Executar testes

```bash
poetry run pytest
```

### Subir documentação local

```bash
mkdocs serve
```

---

## 📚 Documentação

Acesse a documentação completa do projeto:

```text
https://eduardohnsantos.github.io/sales-etl-pipeline/
```

---

## 📌 Próximos Passos

- Integração com PostgreSQL
- Dashboards no Power BI
- Conteinerização com Docker
- Automatização do pipeline
- Evolução da arquitetura

---

## 🔗 GitHub

https://github.com/eduardohnsantos/sales-etl-pipeline
