"""Arquivo principal responsável pela execução do pipeline ETL."""

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import contact_data_frames

if __name__ == "__main__":
    print("Iniciando pipeline ETL...\n")

    data_frame_list = extract_from_excel("data/raw")

    print(f"Arquivos extraídos: {len(data_frame_list)}")

    data_frame = contact_data_frames(data_frame_list)

    print(f"Total de registros consolidados: {len(data_frame)}")

    resultado = load_excel(
        data_frame,
        "data/trusted",
        "trusted",
    )

    print(resultado)

    print("\nPipeline executado com sucesso!")
