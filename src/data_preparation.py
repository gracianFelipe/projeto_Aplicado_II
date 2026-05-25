import pandas as pd

from src.config import PRIMARY_DATASET, PROCESSED_DIR, TEXT_COLUMNS
from src.utils_text import build_text_column


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(PRIMARY_DATASET)

    # Remover duplicidades integrais #
    df = df.drop_duplicates().copy()

    # Manter apenas linhas com rating > 0 para treinamento supervisionado #
    df = df[df["rating"] > 0].copy()

    # Construção do texto consolidado #
    df["text_input"] = build_text_column(df, TEXT_COLUMNS)

    # Remover linhas que fiquem vazias após a limpeza #
    df = df[df["text_input"].str.len() > 0].copy()

    output_path = PROCESSED_DIR / "ifood_feb2021_text_base.parquet"
    df.to_parquet(output_path, index=False)

    print(f"Base processada salva em: {output_path}")
    print(f"Total de linhas após preparação: {len(df):,}")


if __name__ == "__main__":
    main()
