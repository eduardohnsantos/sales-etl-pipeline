from pathlib import Path
from random import choice, randint, uniform
from datetime import datetime, timedelta

import pandas as pd


# ==========================================
# CRIA PASTA data/raw SE NÃO EXISTIR
# ==========================================

RAW_PATH = Path("data/raw")
RAW_PATH.mkdir(parents=True, exist_ok=True)


# ==========================================
# DADOS FAKE
# ==========================================

lojas = [
    "Loja SP",
    "Loja RJ",
    "Loja BH",
    "Loja Curitiba",
    "Loja Salvador",
    "Loja Recife"
]

produtos = {
    "Pizza": [
        "Pizza Calabresa",
        "Pizza Portuguesa",
        "Pizza Frango Catupiry"
    ],
    "Bebida": [
        "Refrigerante",
        "Suco Natural",
        "Água"
    ],
    "Lanche": [
        "Hambúrguer",
        "Cheeseburger"
    ],
    "Acompanhamento": [
        "Batata Frita",
        "Onion Rings"
    ]
}

vendedores = [
    "Carlos",
    "Marina",
    "João",
    "Fernanda",
    "Lucas",
    "Patricia"
]

formas_pagamento = [
    "PIX",
    "Crédito",
    "Débito",
    "Dinheiro"
]


# ==========================================
# FUNÇÃO PARA GERAR DATA ALEATÓRIA
# ==========================================

def gerar_data_aleatoria():
    data_inicio = datetime(2026, 1, 1)
    dias_aleatorios = randint(0, 120)

    return data_inicio + timedelta(days=dias_aleatorios)


# ==========================================
# FUNÇÃO PARA GERAR DATAFRAME
# ==========================================

def gerar_dataframe(loja, quantidade_linhas=500):

    dados = []

    for _ in range(quantidade_linhas):

        categoria = choice(list(produtos.keys()))
        produto = choice(produtos[categoria])

        quantidade = randint(1, 5)

        valor_unitario = round(uniform(8, 120), 2)

        dados.append({
            "data_venda": gerar_data_aleatoria(),
            "loja": loja,
            "produto": produto,
            "categoria": categoria,
            "vendedor": choice(vendedores),
            "quantidade": quantidade,
            "valor_unitario": valor_unitario,
            "forma_pagamento": choice(formas_pagamento)
        })

    return pd.DataFrame(dados)


# ==========================================
# GERAR ARQUIVOS EXCEL
# ==========================================

for loja in lojas:

    df = gerar_dataframe(loja)

    nome_arquivo = (
        loja.lower()
        .replace(" ", "_")
        .replace("ã", "a")
    )

    caminho_arquivo = RAW_PATH / f"vendas_{nome_arquivo}.xlsx"

    df.to_excel(caminho_arquivo, index=False)

    print(f"Arquivo criado: {caminho_arquivo}")


print("\nDados fake gerados com sucesso!")