from fastapi import APIRouter, Depends
from app.models.anomaly import AnomalyInput
from app.services.app_service import process_anomaly
from app.core.security import verify_api_key

router = APIRouter()

@router.post("/anomaly")
def receive_anomaly(
    data: AnomalyInput,
    api_key: str = Depends(verify_api_key)
):
    return process_anomaly(
        metric=data.metric,
        value=data.value,
        source=data.source
    )
