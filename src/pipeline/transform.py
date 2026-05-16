import pandas as pd


"""
função para transformar os dataframes extraídos para um único dataframe
"""

def contact_data_frames(
    data_frame_list: list[pd.DataFrame]
) -> pd.DataFrame:

    # concatena os dataframes
    df = pd.concat(
        data_frame_list,
        ignore_index=True
    )

    total_before = len(df)

    # remove registros duplicados
    df = df.drop_duplicates()

    total_after = len(df)

    print(
        f"Duplicados removidos: "
        f"{total_before - total_after}"
    )

    return df