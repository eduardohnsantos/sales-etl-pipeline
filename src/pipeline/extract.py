"""Módulo responsável pela extração de arquivos Excel."""

import glob
import os

import pandas as pd


def extract_from_excel(path: str) -> list[pd.DataFrame]:
    """
    Extrai arquivos Excel de um diretório.

    Args:
        path (str):
            Caminho da pasta contendo arquivos Excel.

    Returns:
        list[pd.DataFrame]:
            Lista de DataFrames extraídos.
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
