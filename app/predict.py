import joblib
import json
import os
import numpy as np

MODEL_PATH = os.path.join("model", "model.pkl")
COLUMNS_PATH = os.path.join("model", "encoded_columns.json")
THRESHOLD_PATH = os.path.join("model", "threshold.json")


# Chargement des artefacts (au démarrage)
model = joblib.load(MODEL_PATH)

with open(COLUMNS_PATH, "r") as f:
    encoded_columns = json.load(f)

with open(THRESHOLD_PATH, "r") as f:
    threshold = json.load(f)["threshold"]


def prepare_features(features: list):
    """
    Transforme la liste en array avec le bon format
    """
    X = np.array(features).reshape(1, -1)

    if X.shape[1] != len(encoded_columns):
        raise ValueError(
            f"Expected {len(encoded_columns)} features, got {X.shape[1]}"
        )

    return X


def predict_score(features: list):
    """
    Retourne la proba + décision
    """
    X = prepare_features(features)

    proba = model.predict_proba(X)[0][1]

    prediction = int(proba >= threshold)
    decision = "refused" if prediction == 1 else "accepted"

    return {
        "probability": round(float(proba), 4),
        "prediction": prediction,
        "decision": decision,
        "threshold": threshold
    }