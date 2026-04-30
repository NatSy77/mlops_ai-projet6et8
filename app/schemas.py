from pydantic import BaseModel, Field
from typing import List


class ClientData(BaseModel):
    features: List[float] = Field(
        ...,
        description="Liste des variables numériques du client utilisées par le modèle",
        min_length=1
    )


class PredictionResponse(BaseModel):
    probability: float
    prediction: int
    decision: str
    threshold: float
    