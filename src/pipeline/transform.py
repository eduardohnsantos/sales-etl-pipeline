"""Módulo responsável pela transformação de dados."""

import pandas as pd


def contact_data_frames(
    data_frame_list: list[pd.DataFrame],
) -> pd.DataFrame:
    """
    Consolida múltiplos DataFrames em um único DataFrame.

    Args:
        data_frame_list (list[pd.DataFrame]):
            Lista de DataFrames extraídos.

    Returns:
        pd.DataFrame:
            DataFrame consolidado sem registros duplicados.
    """
    df = pd.concat(data_frame_list, ignore_index=True)

    df = df.drop_duplicates()

    return df
