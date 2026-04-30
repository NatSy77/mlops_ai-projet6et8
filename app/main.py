from fastapi import FastAPI

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