import pandas as pd
import joblib

from src.config import MODELS_DIR, PROCESSED_DIR

model = joblib.load(MODELS_DIR / "ifood_text_classifier.joblib")

tfidf = model.named_steps["tfidf"]
clf = model.named_steps["model"]

features = tfidf.get_feature_names_out()
coef = clf.coef_[0]

if clf.classes_[1] != "alta_avaliacao":
    coef = -coef

terms = pd.DataFrame({
    "termo": features,
    "peso": coef
})

positivos = terms.sort_values("peso", ascending=False).head(20)
negativos = terms.sort_values("peso", ascending=True).head(20)

positivos.to_csv(PROCESSED_DIR / "termos_positivos.csv", index=False)
negativos.to_csv(PROCESSED_DIR / "termos_negativos.csv", index=False)

print("Termos positivos:")
print(positivos)

print("\nTermos negativos:")
print(negativos)