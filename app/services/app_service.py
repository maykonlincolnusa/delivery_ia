from app.services.monitoring_service import analyze_anomaly
from app.services.bitrix_service import create_ticket


def process_anomaly(metric, value, source):
    analysis = analyze_anomaly(metric, value)

    if analysis["status"] == "anomaly":
        create_ticket(
            title="Anomalia detectada",
            description=f"""
Métrica: {metric}
Valor: {value}
Origem: {source}
Severidade: {analysis['severity']}
"""
        )

    return analysis
