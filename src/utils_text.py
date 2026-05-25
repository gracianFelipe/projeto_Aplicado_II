import re
import string
import unicodedata
from typing import Iterable

import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Observação: #
# O projeto é em português, então a lista abaixo foi definida manualmente #
# para evitar depender de downloads externos no primeiro uso. #
PT_STOPWORDS = {
    "a", "as", "o", "os", "de", "da", "do", "das", "dos", "e", "em", "no", "na",
    "nos", "nas", "um", "uma", "uns", "umas", "para", "por", "com", "sem", "ao",
    "aos", "à", "às", "que", "se", "ou", "como", "mais", "menos", "muito", "muita",
    "muitos", "muitas", "é", "ser", "são", "foi", "sua", "seu", "seus", "suas",
    "the", "and"
}


def strip_accents(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text))
    return "".join(char for char in text if not unicodedata.combining(char))


def normalize_text(text: str) -> str:
    text = str(text).lower()
    text = strip_accents(text)
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = [
        token for token in text.split()
        if token not in PT_STOPWORDS and len(token) > 1
    ]
    return " ".join(tokens)


def build_text_column(df: pd.DataFrame, text_columns: Iterable[str]) -> pd.Series:
    filled = df[list(text_columns)].fillna("")
    combined = filled.astype(str).agg(" ".join, axis=1)
    return combined.apply(normalize_text)


def create_binary_target(rating_series: pd.Series, threshold: float = 4.5) -> pd.Series:
    return rating_series.apply(lambda rating: "alta_avaliacao" if rating >= threshold else "demais")
