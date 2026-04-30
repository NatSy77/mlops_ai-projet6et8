from fastapi import FastAPI

from app.schemas import ClientData, PredictionResponse
from app.predict import predict_score

app = FastAPI(
    title="Credit Scoring API",
    description="API de prédiction pour le modèle de scoring crédit",
    version="0.1.0"
)


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
    result = predict_score(client_data.features)
    return PredictionResponse(**result)