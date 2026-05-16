import pandas as pd
from typing import List


"""
função para transformar os dataframes extraídos para um único dataframe
"""

def contact_data_frames(data_frame_list: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)