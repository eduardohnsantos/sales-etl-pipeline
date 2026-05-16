import pandas as pd
from pipeline.transform import contact_data_frames


df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

def testar_concatenacao_lista_de_dataframes():
    arrange = pd.concat([df_1, df_2], ignore_index=True)

    act = contact_data_frames([df_1, df_2])

    assert arrange.equals(act)

