"""Módulo responsável pela carga de dados tratados."""

import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame,
    output_path: str,
    file_name: str,
) -> str:
    """
    Salva um DataFrame em um arquivo Excel.

    Args:
        data_frame (pd.DataFrame):
            DataFrame a ser salvo.

        output_path (str):
            Caminho onde o arquivo Excel será salvo.

        file_name (str):
            Nome do arquivo Excel.

    Returns:
        str:
            Mensagem de sucesso ou erro durante o salvamento.
    """
    try:
        os.makedirs(output_path, exist_ok=True)

        output_file = f"{output_path}/{file_name}.xlsx"

        data_frame.to_excel(output_file, index=False)

        return f"Arquivo salvo com sucesso em: {output_file}"

    except Exception as error:
        return f"Erro ao salvar o arquivo: {error}"
