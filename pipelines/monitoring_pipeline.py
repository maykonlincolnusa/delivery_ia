from services.engloba_service import EnglobaService
from services.bitrix_service import BitrixService
from services.s3_service import S3Service
from crew.crew_setup import run_crew

def run_monitoring_pipeline():
    print("📡 Starting monitoring pipeline")

    engloba = EnglobaService()
    deliveries = engloba.get_deliveries()

    bitrix = BitrixService()
    tickets = bitrix.get_open_tickets()

    s3 = S3Service()
    s3.save_raw_data(deliveries, prefix="deliveries")
    s3.save_raw_data(tickets, prefix="tickets")

    run_crew({
        "deliveries": deliveries,
        "tickets": tickets
    })
