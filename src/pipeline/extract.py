import os #bilbioteca para manipular aquivos e diretórios
import glob # biblioteca para listar arquivos

import pandas as pd

from typing import List


"""
funçao para ler os aquivos de uma pasta
data/input e retornar uma lista de dataframes

args: input_path: caminho da pasta onde estão os arquivos csv

return: lista de dataframes
"""

path = "data/raw"

def extract_from_excel(path: str) -> list[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)


