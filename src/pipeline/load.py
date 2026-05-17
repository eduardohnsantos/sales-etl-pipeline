import os

import pandas as pd

"""
receber um dataframe e salvar em um arquivo excel

args:
data_frame (pd.DataFrame): dataframe a ser salvo
output_path (str): caminho onde o arquivo excel será salvo
file_name (str): nome do arquivo excel a ser salvo

return: "Arquivo salvo com sucesso!" ou "Erro ao salvar o arquivo: {error}"
"""


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:

    try:

        # cria a pasta caso não exista
        os.makedirs(output_path, exist_ok=True)

        output_file = f"{output_path}/{file_name}.xlsx"

        data_frame.to_excel(output_file, index=False)

        return f"Arquivo salvo com sucesso em: {output_file}"

    except Exception as e:

        return f"Erro ao salvar o arquivo: {e}"
