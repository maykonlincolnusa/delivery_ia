from pydantic import BaseModel

class AnomalyInput(BaseModel):
    metric: str
    value: float
    source: str
