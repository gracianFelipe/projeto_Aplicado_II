import json

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, confusion_matrix

from src.config import HIGH_RATING_THRESHOLD, MODELS_DIR, PROCESSED_DIR
from src.utils_text import create_binary_target


def main() -> None:
    df = pd.read_parquet(PROCESSED_DIR / "ifood_feb2021_text_base.parquet")
    df["target"] = create_binary_target(df["rating"], threshold=HIGH_RATING_THRESHOLD)

    sample = df.sample(min(20000, len(df)), random_state=42)
    model = joblib.load(MODELS_DIR / "ifood_text_classifier.joblib")
    predictions = model.predict(sample["text_input"])

    cm = confusion_matrix(sample["target"], predictions, labels=["alta_avaliacao", "demais"])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["alta_avaliacao", "demais"])
    disp.plot()
    plt.tight_layout()
    plt.savefig(PROCESSED_DIR / "confusion_matrix.png", dpi=150)
    plt.close()

    results = {
        "sample_accuracy": accuracy_score(sample["target"], predictions),
        "sample_classification_report": classification_report(sample["target"], predictions, output_dict=True),
    }

    with open(PROCESSED_DIR / "evaluation_results.json", "w", encoding="utf-8") as fp:
        json.dump(results, fp, ensure_ascii=False, indent=2)

    print("Avaliação concluída.")
    print(json.dumps({"sample_accuracy": results["sample_accuracy"]}, indent=2))


if __name__ == "__main__":
    main()
