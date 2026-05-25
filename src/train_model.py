import json

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.config import (
    HIGH_RATING_THRESHOLD,
    MIN_DF,
    MODELS_DIR,
    NGRAM_RANGE,
    PROCESSED_DIR,
    RANDOM_STATE,
    TEST_SIZE,
)
from src.utils_text import create_binary_target


def main() -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_parquet(PROCESSED_DIR / "ifood_feb2021_text_base.parquet")
    df["target"] = create_binary_target(df["rating"], threshold=HIGH_RATING_THRESHOLD)

    X_train, X_test, y_train, y_test = train_test_split(
        df["text_input"],
        df["target"],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["target"],
    )

    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(min_df=MIN_DF, ngram_range=NGRAM_RANGE)),
            ("model", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision_macro": precision_score(y_test, predictions, average="macro"),
        "recall_macro": recall_score(y_test, predictions, average="macro"),
        "f1_macro": f1_score(y_test, predictions, average="macro"),
        "classification_report": classification_report(y_test, predictions, output_dict=True),
    }

    with open(PROCESSED_DIR / "metrics.json", "w", encoding="utf-8") as fp:
        json.dump(metrics, fp, ensure_ascii=False, indent=2)

    joblib.dump(pipeline, MODELS_DIR / "ifood_text_classifier.joblib")

    pd.DataFrame({"text_input": X_test, "y_true": y_test, "y_pred": predictions}).to_csv(
        PROCESSED_DIR / "ifood_test_predictions.csv",
        index=False,
    )

    print("Treinamento finalizado.")
    print(json.dumps({k: v for k, v in metrics.items() if k != "classification_report"}, indent=2))


if __name__ == "__main__":
    main()
