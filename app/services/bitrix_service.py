import requests
from app.core.config import settings


def create_ticket(title: str, description: str):
    """
    Cria um ticket no Bitrix24 via webhook
    """
    if not settings.BITRIX_WEBHOOK_URL:
        raise Exception("BITRIX_WEBHOOK_URL não configurado no .env")

    payload = {
        "fields": {
            "TITLE": title,
            "COMMENTS": description
        }
    }

    response = requests.post(
        settings.BITRIX_WEBHOOK_URL,
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()
