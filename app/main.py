from fastapi import FastAPI

from app.schemas import ClientData, PredictionResponse

app = FastAPI(
    title="Credit Scoring API",
    description="API de prédiction pour le modèle de scoring crédit",
    version="0.1.0"
)

THRESHOLD = 0.5


@app.get("/")
def read_root():
    return {
        "message": "Credit Scoring API is running",
        "status": "ok"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(client_data: ClientData):
    """
    Endpoint de prédiction mock.
    Cette version sera remplacée ensuite par le vrai modèle LightGBM.
    """
    probability = sum(client_data.features) / len(client_data.features)

    prediction = int(probability >= THRESHOLD)
    decision = "refused" if prediction == 1 else "accepted"

    return PredictionResponse(
        probability=round(probability, 4),
        prediction=prediction,
        decision=decision,
        threshold=THRESHOLD
    )