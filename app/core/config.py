from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = "QRIA Monitoring API"
    BITRIX_WEBHOOK_URL = os.getenv("BITRIX_WEBHOOK_URL")
    API_KEY = os.getenv("API_KEY")

settings = Settings()
